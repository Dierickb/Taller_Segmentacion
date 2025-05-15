import itk

# Definición del tipo de imagen
PixelType = itk.UC  # Unsigned Char
Dimension = 3
ImageType = itk.Image[PixelType, Dimension]

# Rutas de entrada y salida
image_file = "examples/images/OriginalImages/MRBreastCancer.nii"
output_image_file = "examples/images/OriginalImages/MRBreastCancerRescaled.nii"

def read_image(image_type, input_image_path):
    reader = itk.ImageFileReader[image_type].New()
    reader.SetFileName(input_image_path)
    reader.Update()
    return reader.GetOutput()

def rescaler_image(image, image_type):
    rescaler = itk.RescaleIntensityImageFilter[image_type, image_type].New()
    rescaler.SetInput(image)
    rescaler.SetOutputMinimum(0)
    rescaler.SetOutputMaximum(255)
    rescaler.Update()
    return rescaler.GetOutput()

def write_image(image, image_type, output_image_path):
    writer = itk.ImageFileWriter[image_type].New()
    writer.SetFileName(output_image_path)
    writer.SetInput(image)
    writer.Update()
    print(f"Imagen escrita en: {output_image_path}")

# Ejecución del flujo
image = read_image(ImageType, image_file)
image_rescaled = rescaler_image(image, ImageType)
write_image(image_rescaled, ImageType, output_image_file)
