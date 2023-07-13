import os
import shutil

def extract_file_name(file_path):
    file_name = os.path.basename(file_path)
    name_without_extension = os.path.splitext(file_name)[0]
    return name_without_extension

def move_text_files(directory_a, directory_b):
    for file_a in os.listdir(directory_a):
        file_a_path = os.path.join(directory_a, file_a)
        if os.path.isfile(file_a_path):
            name_without_extension = extract_file_name(file_a_path)
            text_file_path = os.path.join(directory_b, name_without_extension + ".txt")
            if os.path.isfile(text_file_path):
                shutil.move(text_file_path, directory_a)
                print(f"El archivo de texto '{os.path.basename(text_file_path)}' fue movido al directorio A.")


directory_a = ""

directory_b = ""

move_text_files(directory_a, directory_b)
