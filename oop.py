#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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