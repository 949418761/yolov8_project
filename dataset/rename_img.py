import os

# 文件夹路径
folder_path = 'VOCdevkit/Augumentation/images'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 判断文件是否为图片文件（可根据实际情况添加其他判断条件）
    if filename.endswith('.jpeg'):
        # 构建原始文件路径
        original_path = os.path.join(folder_path, filename)

        # 构建新的文件路径（修改后缀名为.png）
        new_path = os.path.join(folder_path, filename[:-4] + '.jpg')

        # 重命名文件
        os.rename(original_path, new_path)
