import os

def list_files(start_path='F:\\codegit\\知识库\\Ultralytics_Markdown_Docs\\Ultralytics_Markdown_Docs'):
    """
    遍历指定起始路径下的所有文件和子目录。
    """
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# 调用函数执行遍历
list_files()