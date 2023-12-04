import os

# 设置文件夹路径
txt_folder = 'labels/train'
img_folder = 'images/train'

# 获取所有txt和jpg文件的文件名（不包括扩展名）
txt_filenames = {name.split('.')[0] for name in os.listdir(txt_folder) if name.endswith('.txt')}
jpg_filenames = {name.split('.')[0] for name in os.listdir(img_folder) if name.endswith('.jpg')}

# 找出不匹配的文件名
unmatched_txt = txt_filenames - jpg_filenames
unmatched_jpg = jpg_filenames - txt_filenames

# 删除不匹配的JPG文件
for filename in unmatched_jpg:
    file_path = os.path.join(img_folder, filename + '.jpg')
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除不匹配的JPG文件: {file_path}")
    else:
        print(f"JPG文件不存在，无法删除: {file_path}")

# 删除不匹配的TXT文件
for filename in unmatched_txt:
    file_path = os.path.join(txt_folder, filename + '.txt')
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除不匹配的TXT文件: {file_path}")
    else:
        print(f"TXT文件不存在，无法删除: {file_path}")
