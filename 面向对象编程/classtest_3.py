class UserData:
    def __init__ (self,id,name):
        self.id = id
        self._name = name

'''    def __repr__(self):
        return self._name
'''

class NewUser(UserData):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(str(value)) > 3:
            self._name = value
        else:
            print("ERROR")
#之前定义的name于装饰器name重名，导致def name 成为一个迭代器，无限迭代
#定义一个_name 私有属性，不能在类的外部调用，只能通过方法属性对其属性进行修改

if __name__ == "__main__":
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
