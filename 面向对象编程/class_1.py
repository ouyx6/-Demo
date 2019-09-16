#!/usr/bin/env python3
class Animal(object):
    owner = 'jack'

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.owner

    @classmethod
    def set_owner(cls,name):
    	cls.owner = name 

