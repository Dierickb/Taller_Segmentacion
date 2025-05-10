import itk
from .Base import Base
from .Filter import Filter

class OtsuThresholding(Base, Filter):
    def __init__(
        self, 
        input_image_path: str,
        file_executed: str, 
        num_bins: int,
        num_thresholds: int,
        label_offset: int,
    ):
        super().__init__(input_image_path, file_executed)

        self.m_num_bins = int(num_bins)
        self.m_num_thresholds = int(num_thresholds) 
        self.m_label_offset = int(label_offset)

    def otsu_threshold_image(self):
        Dimension = 3

        FloatPixelType = itk.ctype("float")
        FloatImageType = itk.Image[FloatPixelType, Dimension]

        input_image = self.read_image(FloatImageType)

        otsu = itk.OtsuMultipleThresholdsImageFilter.New(Input=input_image)
        otsu.SetNumberOfHistogramBins(self.m_num_bins)
        otsu.SetNumberOfThresholds(self.m_num_thresholds)
        otsu.SetLabelOffset(self.m_label_offset)
        
        image_rescaled = self.rescaler_image(FloatImageType, otsu)

        self.write_image(image_rescaled, FloatImageType)

        print(f"Otsu thresholding applied: {self.m_input_image_path} -> {self.m_output_image_path}")