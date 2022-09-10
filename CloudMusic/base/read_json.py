import json
import os
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# sys.path.append(BASE_DIR)


# 读取文件方法
def read_json(filename):
    # 文件路径
    filepath = 'data//' + filename
    # filepath = '../data/' + filename
    # print(filepath)
    # 读入json文件
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


#######################

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# print(os.path.abspath(__file__))

# print(os.getcwd())
# print(os.path.exists(BASE_DIR + '\\data\\login.json'))
# print(BASE_DIR + '\\data\\login.json')
# print(read_json('login.json'))
