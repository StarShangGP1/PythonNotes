#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
/**
 *
 *   █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
 * ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
 * ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
 * ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
 * ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
 *  ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
 *  ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
 *  ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
 *           ░     ░ ░      ░  ░
 */            
'''

from io import StringIO, BytesIO
import os, pickle

print('------文件读写------')

try:
	f = open('test.txt', 'a', encoding='utf8')
	print(f.read())
finally:
	if f:
		f.close()

with open('test.txt', 'r') as f:
	print(f.read())


f = open('test.txt', 'r')
for line in f.readlines():
	print(line.strip())
f.close()
'''
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
'''
f = open('README.md', 'rb')
print(f.read())
f.close()

f = open('README.md', 'r', encoding='utf8', errors='ignore')
print(f.read())
f.close()

f = open('test.txt', 'w')
f.write('python test')
f.close()

with open('test.txt', 'a') as f:
	f.write('\nHelf')


f = StringIO()
f.write('aaaa1')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGood!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
f.close()


f = BytesIO()
f.write('aaa'.encode('utf-8'))
print(f.getvalue())
f.close()

print('------操作文件和目录------')


print(os.name)
print(os.environ.get('PATH'))
print('-----------')

# 查看当前目录的绝对路径:
root = os.path.abspath('.')
print(root)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
testdir = os.path.join(root, 'testdir')
print(testdir)

# 然后创建一个目录:
# os.mkdir(testdir)

# 删掉一个目录:
# os.rmdir(testdir)

# txt = os.path.abspath('./testOne.txt')

# print(os.path.splitext(txt))

# 对文件重命名:
# os.rename('testOne.txt', 'test.txt')

# 删掉文件:
# os.remove('testOne.txt')

print(os.listdir('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])

print('------序列化------')

# d = dict(name='Bob', age=20, score=88)
d = {'name':'Bob', 'age':20, 'score':88}
print(pickle.dumps(d))
# f = open('test.txt', 'wb', encoding='utf8')
# pickle.dump(d, f)
# f.close()
