"""
用于将x文件夹内的东西全移动到父文件夹
"""

import os,shutil,sys
if len(sys.argv)!=3:
    print("Usage: python move_files.py [source_folder] [target_folder]")
    exit(1)

source_folder = sys.argv[1]
target_folder = sys.argv[2]

print(source_folder)

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            yield file,file_path

def copy_file(source_path, destination_path):
    try:
        folder_path = os.path.dirname(destination_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.copyfile(source_path, destination_path)
        return True
    except Exception as e:
        print(f"复制文件失败：{e}")
        return False

for f,f_path in list_files(source_folder):
    if f.endswith(".exe"):
        continue
    tmp=source_folder.split("\\")
    copy_file(f_path, f"{target_folder}\\{tmp[-1]}{f}")
    