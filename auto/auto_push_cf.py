import os
import re
import shutil

folder_path = './code/CodeForce'
target_folder='./Daily_CF_Problems'
target_path='./Daily_CF_Problems/daily_problems'  
NAME="Open17"
pattern = r'\[(.*?)\]'

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            yield file_path

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


print("自动化打卡,启动!")


print("读取文件列表...")
for file_path in list_files(folder_path):
    matches = re.findall(pattern, file_path)
    if matches:
        date_list=matches[-1].split('-')
        if len(date_list)!=3:continue
        dir=date_list[0]+"/"+date_list[1]+"/"+date_list[1]+date_list[2]
        destination_path=os.path.join(target_path,dir)+'/personal_submission/'+re.sub(pattern, '_'+NAME, file_path.split('/')[-1])
        print("自动化打卡生成:   ",destination_path)
        copy_file(file_path, destination_path)
        os.system('cd ' + target_folder + ' && git add . && git commit -m "' + ''.join(date_list) + ' ' + NAME + '\'s submission"')
    

print("自动化打卡完成!")