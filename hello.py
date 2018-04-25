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

# 逗号“,”会输出一个空格
print('11111',22,1,'I','qurck')

#----------------------------------

# 输入
# name = input('请输入任意字符串\n')
# 输出
# print('输出: ', name)

print('I\'m Ok.')

# r'' 字符串不转义
print(r'I\'m Ok.')

# '''...'''的格式表示多行内容
print(''' 
111111111
222222222
333333333''')

print(r'''hello,\n
world''')

#and 与
#or  或
#not 非
#None 空值

# / 除   // 整除  % 余数

# String
# ord()
# chr()
print(ord('A'))
print(chr(65))
# b'xxx' 字节
print(type(b'aaa'))

print('中文'.encode('utf-8'))
print('ABC'.encode('ascii'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore'))
print(b'\xe4\xb8\xad\xe6'.decode('utf-8', errors='ignore'))
print(b'ABC'.decode('ascii'))

# encode() decode()

# len() 字符串长度
print(len('abcd'))

print('------格式化------')

#格式化
# %s 字符串
# %d 整数
# %f 浮点数
# %x 十六进制整数

print('Hello %s' % 'Tom')
print('Hello %d' % 666)
print('Hello %f' % 3.1415926)
# %%
print('Hello %%%.2f' % 3.1415926)

print('Hello {0}, {1:.2f}%'.format('Tom', 17.125))

print('------使用list和tuple------')
# 使用list和tuple

print('------list------')

list = ['Tom', 'Jack', 'Alice']
print(list)
print(len(list))

print('添加')
list.append('Admin')
list.insert(0, 'Mon')
print(list)

print('删除')
list.pop()
print(list)

print('替换')
list[0] = 'Show'
print(list)

print('------tuple------')

tuple = ('Tom', 'Jack', 'Alice')
print(tuple)

tuple_air = ()
print(tuple_air)

tuple_one_elm = (1, )
print(tuple_one_elm)

tuple_variable = ('a', 'b', ['aaa', 'bbb'])
print(tuple_variable)

tuple_variable[2][0] = 'Jack'
tuple_variable[2].append('Tom')
tuple_variable[2].insert(0, 'Mon')
print(tuple_variable)

print('------条件判断------')

a = 20;

if a >= 18:
	print('大于18')
elif a <= 18:
	print('小于18')
else:
	print('默认')


print('------循环------')

name_list = ['Jack.Ma', 'Pony.Ma', 'Serly.Zhang']

for names in name_list:
	print(names)

sum = 0
for x in range(101):
	sum = sum + x
print(sum)
print('------------')

sum = 0
n = 99
while n > 0:
	sum = sum + n
	if sum < 2500:
		print(sum)
		#continue
		break
	# print(sum)
	n = n - 2
print('END') 


print('------使用dict和set------')

print('------dict------')
dict = {'Tom': 10, 'Jack': 20, 'Alice': 30}
print(dict)
print('TT' in dict) # dict 是否有 TT 这个key
print(dict.get('Tom'))

dict.pop('Tom') # 删除
print(dict) 

print('------set------')
set1 = set([1, 2, 3, 3])
print(set1)

set1.add(4) # 添加
set1.remove(3) # 删除
print(set1)

print('------------')
set_one = set([1, 3, 5, 7])
set_two = set([2, 4, 6, 8, 7])

print(set_one & set_two) # 交集
print(set_one | set_two) # 并集

# set_test = set([[1,2], 2, 3])  set 里面不能放 list
