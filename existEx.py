import os
import shutil
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))  #현재 디렉토리 
print(os.path.exists('..')) #상위 디렉토리

name = 'oops.txt'
print('isfile : ', os.path.isfile(name))
print('isdir : ' , os.path.isdir(name))
print('isdir : ' , os.path.isdir('.'))
print('isabs : ' , os.path.isabs(name))
print('isabs : ' , os.path.isabs('/Users/jaegyuhan/PythonEx_1/' + name))

shutil.copy('oops.txt', 'oops_new.txt')
print('isexist',os.path.exists('oops_new.txt'))

os.rename('oops_new.txt', 'oops_new2.txt')
print("isexist oops_new2.txt : ", os.path.exists('oops_new2.txt'))

if not os.path.exists('yikes.txt'):
    os.link('oops.txt', 'yikes.txt')
    os.path.isfile('yikes.txt')

print(os.path.abspath('oops.txt'))

'''
모든 파일과 디렉터리의 컨데이너는 파일시스템이다.(볼륨이라고도 한다.)
'''

import glob
print(glob.glob('m*'))

os.getpgid()