import os
import random
import shutil

src_dir = ''
dst_dir = ''

archivos_imagen = [archivo for archivo in os.listdir(src_dir) if archivo.endswith(('.jpg', '.png', '.jpeg'))]

selected_images = random.sample(archivos_imagen, 205)

for image in selected_images:
    origen = os.path.join(src_dir, image)
    destino = os.path.join(dst_dir, image)
    shutil.move(origen, destino)

print("Se han movido las imágenes seleccionadas al directorio destino.")
