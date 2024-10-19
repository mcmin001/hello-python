import os
import re
from datetime import datetime


def organize_file_to_dir(src_dir: str, dest_dir: str):
    # 遍历目录中的文件
    for filename in os.listdir(src_dir):
        # 匹配文件名中的日期部分
        match = re.search(r'(\d{8})', filename)
        if match:
            date_str = match.group(1)
            # 将日期字符串转换为日期对象
            date = datetime.strptime(date_str, '%Y%m%d')
            # 创建以日期命名的文件夹，如果不存在的话
            date_folder = os.path.join(dest_dir, date.strftime('%Y-%m-%d'))
            if not os.path.exists(date_folder):
                os.makedirs(date_folder)
            # 将文件移动到对应的日期文件夹
            old_path = os.path.join(src_dir, filename)
            new_path = os.path.join(date_folder, filename)
            os.rename(old_path, new_path)