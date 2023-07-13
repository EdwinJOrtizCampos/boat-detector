file_path = ''
replacement_string = ''

with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        modified_line = replacement_string + line.split("/")[-1]
        file.write(modified_line)
    file.truncate()
