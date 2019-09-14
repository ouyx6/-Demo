#!/usr/bin/env python3

class UserData():
    def __init__ (self, num, name):
        self.name = name
        self.num = num

    def __repr__ (self):
        return 'ID:{} Name:{}'.format(self.num, self.name)



if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)

