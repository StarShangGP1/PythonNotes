#!/usr/bin/env python3

# 输入
# input()

# r'' 字符串不转义
# print(r'')

# '''...'''的格式表示多行内容
# print('''xxx''')


#and 与
#or  或
#not 非
#None 空值

# / 除   // 整除  % 余数

# ord()
# chr()
# b'...' 字节

#utf-8 ascii
# encode() decode()

# len() 字符串长度

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序 Windows系统会忽略这个注释
#!/usr/bin/env python3

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，
#否则，你在源代码中写的中文输出可能会有乱码
# -*- coding: utf-8 -*-


#格式化

# %s 字符串
# %d 整数
# %f 浮点数
# %x 十六进制整数  
# format()

# list  有序的集合 列表(数组)  可以添加和删除元素  list = ['1', '2', '3']  就是数组
# tuple 有序的列表 元组 一旦初始化就不能修改  tuple = ('Tom', 'Jack', 'Alice')
# dict  全称dictionary 字典 key-value dict = {'Tom': 10, 'Jack': 20, 'Alice': 30}
# set   和dict类似 也是一组key的集合，但不存储value key不能重复 set = set([1, 2, 3])
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# set的原理和dict一样，所以，同样不可以放入可变对象(list)

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# 所以，dict是用空间来换取时间的一种方法。


# 条件判断
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# if x:
# 	print('Ture')

# 循环
# for val in list:
# 	pass
# range(5)  [0, 1, 2, 3, 4]

# while x:
# 	pass

# continue 跳过这次循环
# break    结束循环


# 函数

def function():
	pass

# isinstance() 数据类型检查

# *numbers 把这个list的所有元素作为可变参数传进去
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
'''
 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
 这5种参数都可以组合使用。但是请注意，
 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L[:3]

# 迭代

'''
d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
	print(k, v)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance(d, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
for k,v in enumerate(d):
	print(k,'----',v)

'''

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

# list、tuple、dict、set、str、generator、包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

# 高阶函数

'''
 map()函数接收两个参数，一个是函数，一个是Iterable(可迭代)，
 map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator(迭代器)返回。
'''
# map()

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
# reduce()

# lambda 匿名函数

'''
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，
也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''
# filter()

# 可以对list进行排序
# sorted()

# 返回函数
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 匿名函数
# 关键字 lambda

# 裝飾器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# functools模块

# 偏函數（Partial function）
# functools.partial


# 模块
# import xxx
# 作用域
# _xxx private
# xxx public

# 安装第三方模块
# pip install xxx
# https://pypi.org/

# 面向对象编程
# 面向对象编程——Object Oriented Programming，简称OOP，是一种"程序设计思想"。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# __name _name _Student__name

# type()
# isinstance()
# dir() 获得一个对象的所有属性和方法

