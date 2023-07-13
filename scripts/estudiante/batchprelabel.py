import os
import shutil

exps = 1
input_data = ""
output_data = ""

nodetect = ""
if not os.path.exists(nodetect):
    os.mkdir(nodetect)

print("\nStarting batch pre-labelling proccess using yolov7.pt [{} -> {}]...\n".format(input_data,output_data))

os.system("python detect.py --weights yolov7.pt --conf-thres 0.25 --img-size 640 --classes 8 --save-txt --source {} --project {}".format(input_data,output_data))

print("\nfinished pre-labeling. Inferences saved to {}\n".format(output_data))

print("\nSaving failed inferences to {}...\n".format(nodetect))

for i in range(exps):
    if i == 0:
        labels = ""
        images = ""
    else:
        labels = "".format(str(i+1))
        images = "{}".format(str(i+1))
    image_files = os.listdir(images)
    labels_files = os.listdir(labels)

    for file_name in image_files:
        if file_name.replace("jpg","txt") not in labels_files and file_name != "labels":
            file_path = os.path.join(images, file_name)
            shutil.move(file_path, os.path.join(nodetect, file_name))
