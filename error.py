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

import logging
import pdb
import unittest
logging.basicConfig(level=logging.DEBUG)

print('------错误处理------')

try:
	print('try...')
	r = 10 / int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

print('------------')

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
		# logging.exception(e)
	else:
		print('no error')
	finally:
		 print('finally...')

main()

print('------------')

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

# foo('2')

def bar():
	try:
		foo('2')
	except ValueError as e:
		print('ValueError!')
		raise

bar()

# try:
# 	10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')


print('------调试------')

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('2')

main()

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

s = '2'
n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

print('------TDD------')

class Dict(dict):
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr(self, key, value):
		self[key] = value

d = Dict(a=1, b=2)
print(d['a'], d.a)

x = 0
y = x if x>0 else 'not zero'
print(y)

