import os
import shutil
from tqdm import tqdm

dir_a_path = ""
dir_b_path = ""
dir_c_path = ""

image_files = [f for f in os.listdir(dir_a_path) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]

for image_file in tqdm(image_files, desc="Copying files", unit="file"):
    if os.path.isfile(os.path.join(dir_b_path, image_file)):
        shutil.copy(os.path.join(dir_b_path, image_file), os.path.join(dir_c_path, image_file))
print()
