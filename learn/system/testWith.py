# -*- coding: utf-8 -*-

class Mycontex(object):
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print("进入enter")
        return self
    def do_self(self):
        print(self.name)
    def __exit__(self,exc_type,exc_value,traceback):
        print("退出exit")
        print(exc_type,exc_value)
if __name__ == '__main__':
    with Mycontex('test') as mc:
        mc.do_self()