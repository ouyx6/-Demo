可迭代对象：可以用for循环迭代的对象
‘’‘
In [1]: letters = ['a', 'b', 'c', 'd', 'e']

In [2]: for letter in letters:
   ...:     print(letter)
   ...:     
a
b
c
d
e
’‘’
迭代器：next 函数去不断获取下一个值，直到返回Stopiteration异常
'‘’
In [6]: it = iter(letters)

In [7]: next(it)
Out[7]: 'a'

In [8]: next(it)
Out[8]: 'b'

In [9]: next(it)
Out[9]: 'c'

In [10]: next(it)
Out[10]: 'd'

In [11]: next(it)
Out[11]: 'e'

In [12]: next(it)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-12-2cdb14c0d4d6> in <module>()
----> 1 next(it)

StopIteration:
‘’‘
迭代器的实现 __iter__和 __next__ 两个方法
‘’'
In [13]: letters
Out[13]: ['a', 'b', 'c', 'd', 'e']

In [14]: it = letters.__iter__()

In [15]: it.__next__()
Out[15]: 'a'

In [16]: it.__next__()
Out[16]: 'b'
'''



