import os
import shutil

src_dir = ""

dst_dir = ""

file_list = ""

valid_exts = [".jpg", ".jpeg", ".png", ".txt"]

with open(file_list, "r") as f:
    files = f.read().splitlines()

for file_path in files:
    file_path = "" + file_path[3:]
    file_path = file_path.split(".")[0] + ".txt"
    file_name = os.path.basename(file_path)
    
    ext = os.path.splitext(file_name)[1]
    if ext not in valid_exts:
        continue
    
    src_path = os.path.join(src_dir, file_name)
    if not os.path.exists(src_path):
        continue
    
    dst_path = os.path.join(dst_dir, file_name)
    shutil.copy2(src_path, dst_path)
