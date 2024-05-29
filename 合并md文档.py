import os


def walk_and_merge(directory, output_file, current_depth=0):
    """
    递归遍历目录，将Markdown文件内容按照目录结构组织并写入到一个文件中。

    :param directory: 起始目录路径
    :param output_file: 输出的Markdown文件路径
    :param current_depth: 当前目录的深度，用于生成标题级别
    """
    with open(output_file, 'a' if os.path.exists(output_file) else 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(directory):
            # 生成当前目录级别的标题
            dir_name = os.path.basename(root)
            title_prefix = "#" * (current_depth + 1) + " "
            out_file.write(title_prefix + dir_name + "\n\n")

            # 处理Markdown文件
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        # 写入文件内容前添加一定数量的'#'以表示文件的层次
                        out_file.write("#" * (current_depth + 2) + " " + file[:-3] + "\n\n")  # 去除.md后缀
                        out_file.write(md_file.read() + "\n\n")  # 内容之后添加空行分隔

            # 递归进入子目录
            for subdir in dirs:
                walk_and_merge(os.path.join(root, subdir), output_file, current_depth + 1)


# 使用示例
output_md_path = 'merged_document.md'
source_directory = 'F:/codegit/知识库/Ultralytics_Markdown_Docs'
walk_and_merge(source_directory, output_md_path)
