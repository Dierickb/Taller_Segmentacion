import os
import sys
import itk
import PIM_T3.Helpers as Helpers

class Base:
    def __init__(self, input_image_path=None, file_executed=None, path_given=True):
        self.m_input_image_path = input_image_path
        self.m_output_image_path = None
        self.path_given = path_given

        if self.path_given:
            if not os.path.isfile(input_image_path):
                raise FileNotFoundError(f"Input image path is invalid or not a file: {input_image_path}")

            self.m_output_image_path = Helpers.ImagePath(input_image_path, file_executed)
            self._confirm_overwrite_if_exists()

    def _confirm_overwrite_if_exists(self):
        if self.path_given and os.path.isfile(self.m_output_image_path):
            respuesta = input(f"El archivo '{self.m_output_image_path}' ya existe. ¿Deseas sobrescribirlo? (y/n): ").strip().lower()
            if respuesta != 'y':
                print("Operación cancelada por el usuario.")
                sys.exit(0)

    def get_input_path(self):
        return self.m_input_image_path

    def get_output_path(self):
        return self.m_output_image_path

    def read_image(self, image_type):
        if not self.path_given:
            raise RuntimeError("No se puede leer imagen: path_given=False")
        reader = itk.ImageFileReader[image_type].New()
        reader.SetFileName(self.m_input_image_path)
        reader.Update()
        return reader.GetOutput()

    def write_image(self, image, image_type):
        if not self.path_given or not self.m_output_image_path:
            raise RuntimeError("No se puede escribir imagen: path_given=False o path no definido")
        writer = itk.ImageFileWriter[image_type].New()
        writer.SetFileName(self.m_output_image_path)
        writer.SetInput(image)
        writer.Update()
        print(f"Imagen escrita en: {self.m_output_image_path}")
