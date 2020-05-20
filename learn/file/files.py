# -*- coding: utf-8 -*-

import time

def file_close():
    try:
        file = open('../gui/pygame.py', 'r')
        print(file.read())
    except IOError:
        print('无法打开指定的文件!')
    finally:
        if file:
            file.close()

def file_with():
    try:
        with open('../gui/pygame.py', 'r') as file:
            print(file.read())
    except IOError:
        print('无法打开指定的文件!')

def for_in():
    # 一次性读取整个文件内容
    with open('../gui/pygame.py', 'r') as file:
        print(file.read())

    # 通过for-in循环逐行读取
    with open('../gui/pygame.py', 'r') as file:
        for line in file:
            print(line)
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('../gui/pygame.py', 'r') as file:
        lines = file.readlines()
    print(lines)

if __name__ == '__main__':
    # file_close()
    # file_with()
    for_in()