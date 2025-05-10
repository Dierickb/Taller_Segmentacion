import itk

class Filter:

    def __init__(self):
        super().__init__()

    def curvatureAnisotropicDiffusionImageFilterPython(
        self,
        input,
        timeStep,
        numberOfIterations,
        conductanceParameter,
        getOutput=True,
    ):
        smoothing = itk.itkCurvatureAnisotropicDiffusionImageFilterPython.New(
            Input=input,
            TimeStep=timeStep,
            NumberOfIterations=numberOfIterations,
            ConductanceParameter=conductanceParameter,
        )
        if getOutput:
            smoothing.Update()
            return smoothing.GetOutput()
        return smoothing
        
    def gradientMagnitudeRecursiveGaussianImageFilter(
        self,
        input,
        sigma,
        getOutput=True,
    ):
        gradient = itk.itkGradientMagnitudeRecursiveGaussianImageFilterPython.New(
            Input=input,
            Sigma=sigma,
        )
        if getOutput:
            gradient.Update()
            return gradient.GetOutput()
        return gradient
    
    def rescaler_image(self, image_type, threshold_filter):
        rescaler = itk.RescaleIntensityImageFilter[image_type, image_type].New()
        rescaler.SetInput(threshold_filter)
        rescaler.SetOutputMinimum(0)
        rescaler.SetOutputMaximum(255)
        rescaler.Update()
        return rescaler.GetOutput()
    
    def statisticsImageFilter(self, input, getOutput=True):
        stats = itk.StatisticsImageFilter.New(Input=input)
        if getOutput:
            stats.Update()
            return stats.GetOutput()
        return stats
    
    def sigmoidImageFilter(self, input, output_minimum, output_maximum, alpha_sigmoid, beta_sigmoid, set_alpha=-0.01, set_beta=20.0 , getOutput=True):
        sigmoid = itk.SigmoidImageFilter.New(
            Input=input,
            OutputMinimum=output_minimum,
            OutputMaximum=output_maximum,
            Alpha=float(alpha_sigmoid),
            Beta=float(beta_sigmoid),
        )
        sigmoid.SetAlpha(set_alpha)
        sigmoid.SetBeta(set_beta)
        sigmoid.Update()
        return sigmoid.GetOutput()
    
    def fastMarchingImageFilter(self, sigmoid, seed, input_image , FloatImageType, stopping_value, getOutput=True):

        fastMarching = itk.FastMarchingImageFilter[FloatImageType, FloatImageType].New(Input=sigmoid)
        fastMarching.SetTrialPoints(seed)
        fastMarching.SetOutputSize(input_image.GetOutput().GetBufferedRegion().GetSize())
        fastMarching.SetStoppingValue(stopping_value)
        
        if getOutput:
            fastMarching.Update()
            return fastMarching.GetOutput()

        return fastMarching
