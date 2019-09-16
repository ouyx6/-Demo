#!/usr/bin/env python3

class UserData:
    def __init__ (self, num, name):
        self.num = num
        self.name = name
    def set_name(self, value):
        self.name = value
    def __repr__(self):
        return "ID:{} Name:{}".format(self.num, self.name)
    

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def __init__(self,num,name):
        UserData.__init__(self,num,name)
    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id,name):
        return "{}'s id is {}".format(name,id)


if __name__ == "__main__":
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
