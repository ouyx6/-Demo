#!/usr/bin/env python3

class Animal:
    def __init__(self):
        self.__age = 3
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self.__age = value
        else:
            raise ValueError
    @age.deleter
    def age(self):
    	print('delect age')
    	del self.__age




