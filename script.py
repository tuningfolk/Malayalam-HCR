import os
import shutil
source = 'dataset'
dest = 'alphabet'

#Creat dest if doesn't exist
if not os.path.exists(dest):
    os.makedirs(dest)

for folder_name in os.listdir(source):
    folder_path = os.path.join(source, folder_name)
    if not os.path.isdir(folder_path): continue
    files = os.listdir(folder_path)
    source_image_path = os.path.join(folder_path, files[0])
    # print(files[0][:-4])
    dest_image_path = os.path.join(dest, f"{folder_name}.png")
    shutil.copy(source_image_path, dest_image_path)
print("Process completed.")