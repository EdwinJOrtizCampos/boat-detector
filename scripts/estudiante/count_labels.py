import os

def count_occurrences(directory_path):
    occurrences = {}
    total_count = 0
    cnt = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            cnt += 1
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r") as file:
                for line in file:
                    x_value = int(line.split()[0])
                    if x_value not in occurrences:
                        occurrences[x_value] = 1
                    else:
                        occurrences[x_value] += 1
                    total_count += 1

    percentages = {}
    for x_value, count in occurrences.items():
        percentages[x_value] = count/total_count*100
    print(cnt)
    return percentages

directory_path = ""
percentages = count_occurrences(directory_path)
print(percentages)
