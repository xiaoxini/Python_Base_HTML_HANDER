# coding=utf-8
"""
文本块生成器
思考：
（1）考虑其他的实现方法
（2）可否不用lines生成器，直接在Block生成器中使用文件迭代器："for line in file:" ?
"""

def lines(file):
    for line in file:
        yield line
    yield '\n'            # 在文件末尾添加空行


def Block(file):
    block = []
    for line in lines(file):
        if line.strip():  # 如果去除两边的空格之后，该行不为空，则将它添加到当前块中
            block.append(line)
        elif block:       # 遇到空行，且当前块不空，则进行生成输出
            yield ''.join(block).strip()
            block = []



