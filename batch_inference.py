import os

image_directory = "inference/images/"
command = "python detect.py --weights /opt/qaisc/home/eortiz/edwin/models/yolov7-main/runs/train/BoatsV3_yolov7e6/weights/best.pt --conf 0.25 --img-size 640 --source "

# Get a list of files in the image directory
files = os.listdir(image_directory)

# Filter only image files
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Execute the command for each image file
try:
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        full_command = command + image_path
        os.system(full_command)
except:
    exit()
