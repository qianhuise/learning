import os
import shutil


def merge_md_across_subdirectories(input_dir='F:\\codegit\\知识库\\Ultralytics_Markdown_Docs\\Ultralytics_Markdown_Docs',
                                   output_dir='F:\\codegit\\知识库\\Ultralytics_Markdown_Docs\\merged_docs'):
    """
    将指定目录下每个一级目录及其子目录中的所有Markdown文件合并成一个文件，并以该一级目录名为文件名保存。
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 遍历一级目录
    for item in os.scandir(input_dir):
        if item.is_dir():  # 确保是目录
            subdir_name = item.name
            # 构建输出文件的完整路径
            output_filepath = os.path.join(output_dir, subdir_name + ".md")
            # 初始化合并内容的列表
            all_contents = []

            # 遍历当前一级目录及其所有子目录下的Markdown文件
            for root, _, files in os.walk(item.path):
                for file in files:
                    if file.endswith('.md'):
                        input_filepath = os.path.join(root, file)
                        # 读取Markdown内容
                        with open(input_filepath, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # 移除可能存在的多余空白行（根据需要调整）
                            content = content.strip() + "\n\n"
                            all_contents.append(content)  # 收集内容

            # 写入所有收集到的内容到输出文件
            with open(output_filepath, 'w', encoding='utf-8') as outfile:
                outfile.writelines(all_contents)


# 调用函数执行
merge_md_across_subdirectories()