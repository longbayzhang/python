# -*- coding: utf-8 -*-

import os, shutil, glob, sys, re

def main():
    cwd = os.getcwd()

    print os.chdir(cwd)

    os.system('mkdir python')
    print 'make directory python'

    print os.listdir(cwd)

    if 'python' in os.listdir(cwd):
        print 'python is in ' + os.getcwd()
        print 'delete python directory'
        os.rmdir('python')

    print os.listdir(cwd)

    print dir(os)

    print shutil.copy('system.py', 'system.txt')

    print shutil.move('system.txt', 'backup.py')

    print glob.glob('*.py')

    print sys.argv

    sys.stderr.write('Warning, log file not found starting a new one\n')

    print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    print re.sub(r'(\b[a-z]+)\1', r'\1', 'cat in the the hat cat')

    print 'tea for too'.replace('too', 'two')
if __name__ == '__main__':
    main()