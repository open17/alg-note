import os
import shutil

def delete_cph_folders(root_dir):
    # 遍历根目录及其所有子目录
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # 检查是否有名为 .cph 的文件夹
        for dirname in dirnames:
            if dirname == '.cph':
                folder_path = os.path.join(dirpath, dirname)
                print(f"正在删除文件夹: {folder_path}")
                shutil.rmtree(folder_path)  # 删除文件夹及其所有内容

if __name__ == "__main__":
    # 获取当前脚本的运行路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    delete_cph_folders(current_dir)
