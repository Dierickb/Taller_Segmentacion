import itk
from .Base import Base

class WaterSheed(Base):
    def __init__(
        self, 
        input_image_path: str, 
        file_executed: str,
        threshold: float,
        level: float,
    ):
        super().__init__(input_image_path, file_executed)

        self.m_threshold = threshold
        self.m_level = level

    def watershed_image(self):
        Dimension = 3

        FloatPixelType = itk.ctype("float")
        FloatImageType = itk.Image[FloatPixelType, Dimension]

        input_image = self.read_image(FloatImageType)

        gradientMagnitude = itk.GradientMagnitudeImageFilter.New(Input=input_image)

        watershed = itk.WatershedImageFilter.New(Input=gradientMagnitude.GetOutput())
        watershed.SetThreshold(self.m_threshold)
        watershed.SetLevel(self.m_level)

        LabeledImageType = type(watershed.GetOutput())

        PixelType = itk.ctype("unsigned char")
        RGBPixelType = itk.RGBPixel[PixelType]
        RGBImageType = itk.Image[RGBPixelType, Dimension]

        colormap = itk.ScalarToRGBColormapImageFilter[
            LabeledImageType, RGBImageType
        ].New()
        colormap.SetColormap(
            itk.ScalarToRGBColormapImageFilterEnums.RGBColormapFilter_Jet
        )
        colormap.SetInput(watershed.GetOutput())
        colormap.Update()

        self.write_image(colormap.GetOutput(), RGBImageType)