import itk
from .Base import Base


class BinaryThresholding(Base):
    def __init__(
        self, 
        input_image_path: str | None = None, 
        file_executed: str | None = None,
        upper_threshold: float = 255, 
        lower_threshold: float = 0.0, 
        outside_value: int = 0,
        inside_value: int = 255,
        printing: bool = True,
        path_given: bool = True,
        input_image=None,  # imagen ITK directa si no se usa path
    ):   
        super().__init__(input_image_path, file_executed, path_given)

        self.m_lower_threshold = lower_threshold
        self.m_upper_threshold = upper_threshold
        self.m_outside_value = outside_value
        self.m_inside_value = inside_value
        self.m_printing = printing
        self.image = input_image  # imagen ITK directa

    def threshold_image(self):
        PixelType = itk.UC
        Dimension = 3
        ImageType = itk.Image[PixelType, Dimension]

        if self.path_given:
            input_image = self.read_image(ImageType)
        else:
            if self.image is None:
                raise ValueError("No se ha proporcionado una imagen de entrada.")
            input_image = self.image
        
        threshold_filter = itk.BinaryThresholdImageFilter[ImageType, ImageType].New()
        threshold_filter.SetInput(input_image)
        threshold_filter.SetLowerThreshold(int(self.m_lower_threshold))
        threshold_filter.SetUpperThreshold(int(self.m_upper_threshold))
        threshold_filter.SetOutsideValue(self.m_outside_value)
        threshold_filter.SetInsideValue(self.m_inside_value)
        threshold_filter.Update()

        if self.path_given:
            self.write_image(threshold_filter.GetOutput(), ImageType)

        if self.m_printing:
            print("Binary thresholding aplicado.")

        return threshold_filter.GetOutput()
