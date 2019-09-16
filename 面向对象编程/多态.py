#!/usr/bin/env python3
class Animal(object):
	def __init__(self,name):
		self.name = name
	def set_name(self):
		return self.name
	def make_sound (self):
		pass

class Dog(Animal):
	def make_sound(self):
		print(self.name + ' is making sound wang wang...')
class Cat(Animal):
	def make_sound(self):
		print(self.name + ' is making sound miu miu...')

animals = [Dog('wangcai'), Cat('kitty'), Dog('laifu'), Cat('tom')]
for animal in animals:
	animal.make_sound()