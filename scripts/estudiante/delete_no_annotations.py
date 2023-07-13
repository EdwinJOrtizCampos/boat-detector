import os

dir_path = ''

for file in os.listdir(dir_path):
    try:
        if file.endswith('.txt'):
            print("leyendo {}".format(file))
            basename, extension = os.path.splitext(file)
            image = os.path.join(dir_path, f'{basename}.{extension[1:]}')
            with open(os.path.join(dir_path, file), 'r') as f:
                content = f.read()
                if content == '':
                    os.remove(os.path.join(dir_path, file))
                    os.remove(image)
                    print(f'Se han borrado {file} y {image}')
    except FileNotFoundError as err:
        continue
