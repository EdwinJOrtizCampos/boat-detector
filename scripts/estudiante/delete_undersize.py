import os

undersized_images = ""
images = ""

dir_a_files = os.listdir(undersized_images)

for filename in os.listdir(images):
    filepath = os.path.join(images, filename)
    if os.path.isfile(filepath) and filename in dir_a_files:
        os.remove(filepath)
        print(f"{filename} borrado de {images}.")
