import os
import shutil
import random
import string

src_dir = ""
dest_dir = ""

def extract(src):
    for file in os.listdir(src):
        new_path = os.path.join(src,file)
        if os.path.isdir(new_path):
            print("extrayendo ", file)
            extract(new_path)
        elif file.endswith((".jpeg", "png", "jpg", "JPEG")):
            print("procesando: ", file)
            rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            file_ext = os.path.splitext(file)[1]
            new_file = file.replace(file_ext, '') + '_' + rand_str + file_ext
            print("generado: ", new_file)
            src_path = os.path.join(src, file)
            dest_path = os.path.join(dest_dir, new_file)
            shutil.copy(src_path, dest_path)
        else:
            continue
    return

extract(src_dir)
