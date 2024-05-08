import os
import json
from pathlib import Path
from datetime import datetime

def generate_statistics(directory, output_filename):
    white_list = ['duipai']
    type_count = {}
    date_count = {}

    temp_file = 'temp_git_output.txt'

    # 遍历目录中的所有文件
    for filepath in Path(directory).rglob('*'):
        if filepath.suffix in ['.py', '.cpp'] and filepath.is_file():
            type = filepath.parent.name
            if type not in white_list:
                # 构造并执行 Git 命令，输出重定向到临时文件
                command = f'git log --format=%ai -- "{filepath.as_posix()}"  > {temp_file}'
                os.system(command)

                # 读取临时文件中的输出
                try:
                    with open(temp_file, 'r') as file:
                        first_line = file.readline().strip()
                        print(first_line)
                        birth_date = datetime.strptime(first_line, '%Y-%m-%d %H:%M:%S %z').strftime('%Y-%m-%d')
                except Exception as e:
                    print(e)
                    # 如果读取文件失败或日期解析失败，使用文件系统的创建日期
                    birth_date = datetime.fromtimestamp(filepath.stat().st_ctime).strftime('%Y-%m-%d')
                # 更新类型统计
                type_count[type] = type_count.get(type, 0) + 1
                # 更新日期统计
                date_count[birth_date] = date_count.get(birth_date, 0) + 1

    # 清理临时文件
    # os.remove(temp_file)
    print("cout",date_count)
    # 将统计结果保存到 JSON 文件中
    statistics = {'type_count': type_count, 'date_count': date_count}
    with open(output_filename, 'w') as f:
        json.dump(statistics, f, indent=2)

    print('Statistics JSON has been saved.')

# 调用函数
generate_statistics('./code', 'statistics.json')
