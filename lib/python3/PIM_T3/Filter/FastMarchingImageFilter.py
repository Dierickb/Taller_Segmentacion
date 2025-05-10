import itk
from .Base import Base
from .Filter import Filter
from .BinaryThresholding import BinaryThresholding

class FastMarchingImageFilter(Base, Filter):
    def __init__(
        self, 
        input_image_path: str, 
        file_executed: str,
        sigma: float,
        alpha_sigmoid: float = None,
        beta_sigmoid: float = None,
        x_position: int = 0,
        y_position: int = 0,
        z_position: int = 0,
        stop: float = 100.0,
        time_threshold: float = 20.0,
        auto_sigmoid: bool = False,
        printing: bool = True
    ):
        super().__init__(input_image_path, file_executed)

        self.m_sigma = sigma
        self.alpha_sigmoid = alpha_sigmoid
        self.beta_sigmoid = beta_sigmoid
        self.m_x_position = x_position
        self.m_y_position = y_position
        self.m_z_position = z_position
        self.m_stop = stop
        self.m_time_threshold = time_threshold
        self.auto_sigmoid = auto_sigmoid
        self.m_printing = printing

    def fast_marching_image(self):
        Dimension = 3
        FloatPixelType = itk.ctype("float")
        FloatImageType = itk.Image[FloatPixelType, Dimension]

        input_image = self.read_image(FloatImageType)

        # Filtros
        smoothing = self.curvatureAnisotropicDiffusionImageFilterPython(
            input_image,
            timeStep=0.125,
            numberOfIterations=5,
            conductanceParameter=1.0,
            getOutput=False,
        )

        gradient = self.gradientMagnitudeRecursiveGaussianImageFilter(
            Input=smoothing,
            Sigma=self.m_sigma,
        )

        rescaled = self.rescaler_image(FloatImageType, gradient)

        # Estadísticas del gradiente
        stats = self.statisticsImageFilter(rescaled)
        min_grad = stats.GetMinimum()
        max_grad = stats.GetMaximum()
        mean_grad = stats.GetMean()

        # Calcular alpha y beta si se activa el modo automático
        if self.auto_sigmoid or self.alpha_sigmoid is None or self.beta_sigmoid is None:
            self.beta_sigmoid = mean_grad
            self.alpha_sigmoid = -10.0 / (max_grad - min_grad + 1e-5)
            if self.m_printing:
                print(f"[auto_sigmoid] Alpha: {self.alpha_sigmoid:.4f}, Beta: {self.beta_sigmoid:.4f}")

        sigmoid = self.sigmoidImageFilter(
            rescaled,
            output_minimum=0.0,
            output_maximum=1.0,
            alpha_sigmoid=self.alpha_sigmoid,
            beta_sigmoid=self.beta_sigmoid
        )

        # Semilla
        NodeType = itk.LevelSetNode[FloatPixelType, Dimension]
        NodeContainer = itk.VectorContainer[itk.UI, NodeType]
        seed = NodeContainer.New()

        seed_position = [self.m_x_position, self.m_y_position, self.m_z_position]
        node = itk.LevelSetNode[itk.F, Dimension]()
        index = itk.Index[Dimension]()
        for i in range(Dimension):
            index[i] = seed_position[i]

        node.SetValue(0.0)
        node.SetIndex(index)
        seed.Initialize()
        seed.InsertElement(0, node)

        # Fast Marching
        fastMarching = self.fastMarchingImageFilter(
            sigmoid,
            seed,
            input_image,
            FloatImageType,
            self.m_stop
        )

        fastMarching_output = fastMarching.GetOutput()

        # Umbral binario posterior
        thresholder = BinaryThresholding(
            input_image=fastMarching_output,
            upper_threshold=self.m_time_threshold,
            printing=False,
            path_given=False
        )
        binary_output = thresholder.threshold_image()

        # Escritura del resultado
        self.write_image(binary_output, itk.Image[itk.UC, Dimension])

