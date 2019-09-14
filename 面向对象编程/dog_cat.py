#!/usr/bin/env python3

class Dog(object):
        def __init__(self, name):
                self.name = name

        def get_name(self):
                return self.name
        def set_name(self, value):
                self.name = value
        def bark(self):
                print(self.get_name() + ' is making sound wang wang...')
class Cat(object):
        def __init__(self, name):
                self.name = name
        def get_name(self):
                return self.name.lower().capitalize()
        def set_name(self, value):
                self.name = value
        def mew(self):
                print(self.get_name() + ' is making sound miu miu...')


dog = Dog('king')
cat = Cat('kitty')
dog.bark()
cat.mew()
