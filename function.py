#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
from functools import reduce
import os, time, functools

print(max(4, 5, 6))

def test_function():
	print('asasasa')

test_function()

# 空函数
def nop():
	pass

# isinstance() 数据类型检查
print(isinstance('a', (int, float)))

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(2, 3))

'''
 **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
 kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
 extra = {'city': 'Beijing', 'job': 'Engineer'}
 person('Jack', 24, **extra)
 name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
'''

print('------------')

# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n * fact(n-1)

# print(fact(3))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))

print('------切片------')

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[::3])

temp = list(range(100))
print(temp[::10])

print('------------')

d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
	print(k, v)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance(d, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
for k,v in enumerate(d):
	print(k,'----',v)


print('------列表生成式------')

L_list = list(range(1, 6))
print(L_list)

L_temp = []
for x in range(1,6):
	L_temp.append(x*x)

print(L_temp)

tmp = [x*x for x in range(1,11)]

print(tmp)

test = ['a', 'b', 'c', 'd']

print([x*3 for x in test])

print([x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

arr = []
for m in 'ABC':
	for n in 'XYZ':
		arr.append(m + n)

print(arr)

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

print([s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']])

print('------生成器------')

L = [x * x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)
# print(next(g))

print([n for n in g])

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print([x for x in fib(6)])

print('------迭代器------')

print(isinstance([], Iterable))

print(isinstance(iter([]), Iterable))

print('------高阶函数------')

print(print)

def f(x):
	return x * x

map_list = list(map(f, [1, 2, 3, 4, 5]))
map_str = list(map(str, [1, 2, 3, 4, 5]))

print(map_list)
print(map_str)

def add(x, y):
	return x + y

print(reduce(add, [1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))

def fn(x, y):
	return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[s]

print(int('13579'))
print(reduce(fn, map(char2num, '13579')))

print('------------')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
	def fn(x, y):
		return x * 10 +y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))


print(str2int(DIGITS))
print(type(str2int(DIGITS)))

print('------------')

def char2num(s):
	return DIGITS[s]

def str2int_pro(s):
	return reduce(lambda x, y: x * 10 +y, map(char2num, s))

print(str2int_pro('246810'))
print(type(str2int_pro('246810')))

print('------filter------')

def is_odd(n):
	return n % 2 == 0

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['', '1', '2', '3  ', '5', ' aa', 'a a a ', '  '])))

print('------sorted------')

print(sorted([36, 5, -12, 9, -21]))

# 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

print('-----返回函数------')

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

fun = lazy_sum(1, 3, 5, 7, 9)
fun_2 = lazy_sum(1, 3, 5, 7, 9)

print(fun)
print(fun_2)
print(fun())
print(fun == fun_2)


def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print(f1, '\n', f2, '\n', f3) 
print(f1(), '\n', f2(), '\n', f3()) 

def count_pro():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count_pro()

print(f1, '\n', f2, '\n', f3) 
print(f1(), '\n', f2(), '\n', f3()) 

print('------匿名函数------')

print(list(map(lambda x: str(x), [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = lambda x : x + x

print(f)
print(f(5))

def build(x, y):
	return lambda : x*y
f = build(2, 3)
print(f())

print('------裝飾器-------')


def now():
	print(time.asctime( time.localtime(time.time()) ))
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
aa = now
print(aa)
aa()

print(now.__name__)
print(aa.__name__)

print('------------')

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

# @log
# def now():
# 	print(time.time())

# now()

# now = log(now)
# now()

def log_pro(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

def log_pro_2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# now = log_pro(now)
# now()

now_tmp = log_pro_2('execute')(now)
now_tmp()


print('------偏函數------')

def int2(x, base=2):
	return int(x, base)

print(int2('100'))

int2 = functools.partial(int, base=2)
print(int2('01010'))