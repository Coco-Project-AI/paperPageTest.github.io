import os
import re

# 要处理的目录
dir_path = "./"  # 修改成你的目录路径

# 匹配 XML 标签
xml_pattern = re.compile(r'(<[^>]+>)')

def process_content(content):
    # 用正则分割成 标签 和 文本 两类
    parts = xml_pattern.split(content)

    lines = []
    for part in parts:
        part = part.strip()
        if not part:  # 跳过空
            continue
        lines.append(part)

    # 每个部分独占一行
    return "\n".join(lines)

for filename in os.listdir(dir_path):
    if filename.lower().endswith(".txt"):
        file_path = os.path.join(dir_path, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            raw_content = f.read()

        processed_content = process_content(raw_content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(processed_content)

        print(f"已处理: {filename}")

print("批量处理完成！")

