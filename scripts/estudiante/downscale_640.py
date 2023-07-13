import os
from PIL import Image

def resize_images(directory):
    file_list = os.listdir(directory)

    for filename in file_list:
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and any(file_path.endswith(extension) for extension in ['.jpg', '.jpeg', '.png']):
            try:
                image = Image.open(file_path)

                resized_image = image.resize((640, 640))

                resized_image.save(file_path)

                print(f"reescalado de {filename} exitoso.")
            except Exception as e:
                print(f"Error escalando {filename}: {e}")
        else:
            print(f"{filename} no es un fichero válido.")

directory_path = ""

resize_images(directory_path)
