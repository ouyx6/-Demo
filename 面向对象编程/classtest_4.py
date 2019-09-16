#!/usr/bin/env python3
class UserData():
    def __init__(self,id,name):
        self._id = id
        self._name = name
    '''def __repr__(self):
        return self._name
        '''
class NewUser(UserData):
    def __init__(self,id,name):
        UserData.__init__(self,id,name)

    def __call__(self):
        print('{}\'s id is {}'.format(self._name,self._id)



if __name__ == '__main__':
    user = NewUser(101,'Jack')
    user()
