import os

dir_to_search = ''

for file in os.listdir(dir_to_search):
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        basename, extension = os.path.splitext(file)
        text_file = os.path.join(dir_to_search, f'{basename}.txt')
        if not os.path.isfile(text_file):
            os.remove(os.path.join(dir_to_search, file))
            print(f'Se ha borrado {file}')
