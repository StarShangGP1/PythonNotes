#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType
from enum import Enum, unique
from hello import hello

print('------模块------')

print('------oop------')

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print("%s: %s" % (self.__name, self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
 		# if 0 <= score <= 100:
            self.__score = score
        # else:
            # raise ValueError('bad score')

tom = Student('Math gg', 88)
jack = Student('enligsh', 55)
tom.print_score()
jack.print_score()
print(tom, '\n', jack, '\n', Student)
print(tom.get_grade(), '\n', jack.get_grade())
print(tom.get_score())
tom.set_score(101)
print(tom.get_score())
print(tom._Student__name)

print('------------')

class Animal(object):
	name = 'ssss'
	def run(self):
		print('%s is running...' % self.__class__.__name__)
	def run_twice(self, animal):
		animal.run()
	def fuck_xxx():
		print('fuck xxx')

class Cat(Animal):
	pass

class Dog(Animal):
	pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(issubclass(Cat, Animal))

cat.run_twice(Cat())

print(type(cat))

print(dir(Animal()))
cat.age = 20
print(cat.age)
print(dir(Cat()))

del cat.age
print(cat)

print('------__slots__------')

class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Tom'
print(s.name)

def set_age(self, age):
		self.age = age

# s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
# s.set_age(25)
# print(s.age)

# 给class绑定方法
Student.set_age = MethodType(set_age, Student)


class Students(object):

	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self.__score = value
s1 = Students()
s1.score = 60 # OK，实际转化为s.set_score(60)
print(s1.score) # OK，实际转化为s.get_score()

print()
print('-------多重继承-------')

class CarnivorousMixIn(object):
	pass

class HerbivoresMixIn(object):
	pass

class RunnableMixIn(object):
	def run(self):
		print('running...')

class FlyableMixIn(object):
	def fly(self):
		print('flying...')

class Animal(object):
	pass

class Mammal(object):
	pass

class Bird(Animal):
	pass

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass

class Bat(Mammal, FlyableMixIn, HerbivoresMixIn):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass


print()
print('-------定制类-------')

class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
	 	return self.name
	__repr__ = __str__

print(Student('Toms'))
print(Student.__repr__.__name__)

class Chain(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	def __call__(self):
		print('call me')

	__repr__ = __str__

print(Chain().status.user.timeline.list)
s = Chain()
s()

print(callable(s))

print()
print('-------使用枚举类-------')


Month = Enum('Month', (
	'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
	'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
	))
print(Month)
print(dir(Month))

print([name for name, member in Month.__members__.items()])

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

print('------------')

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

for name, member in Weekday.__members__.items():
	print(name, '=>', member)

print()
print('------使用元类------')

class App(object):
	def run(self):
		print('app is running...')

def fn(self, name='world'):
	print('Hello, %s.' % name)

Hello = type('Hello', (App, ), dict(hello=fn, age=20))

print(Hello)
h = Hello()
h.run()
h.hello()
print(h.age)
print(dir(Hello))