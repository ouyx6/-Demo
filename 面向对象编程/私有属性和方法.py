#!/usr/bin/env python3
class Shiyanlou:
    __private_name = 'shiyanlou'
    public_name = 'hello world'
    def __get_private_name(self):
        return self.__private_name
    def get_public_name(self):
        return self.public_name

s = Shiyanlou()
#orders = [s.__get_private_name, s.get_public_name]

#for order in orders:
#    try:
#        order
#    except AttributeError:
 #       print("you have no admit to get this data")

try:
    print(s._Shiyanlou__private_name)
except AttributeError:
    print("you have no admit to get this data")

    

