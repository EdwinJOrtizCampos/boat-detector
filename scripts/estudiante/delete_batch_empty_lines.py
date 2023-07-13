import os

file_path = ''

result_path = ''

existing_paths = []

with open(file_path, 'r') as f:
    for line in f:
        line2 = line
        line2 = line2.strip()
        line2 = "" + line2[4:]
        if os.path.isfile(line2):
            existing_paths.append(line)

with open(result_path, 'w') as f:
    f.write(''.join(existing_paths))
