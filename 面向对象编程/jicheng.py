class Animal(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self):
        self.name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang...')


class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' is makng sound miu miu...')


dog = Dog('king')
cat = Cat('kitty')
dog.make_sound()
cat.make_sound()

