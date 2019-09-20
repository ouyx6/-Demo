
切片
'''
In [3]: letters = [1, 2, 3, 4, 5, 6,7]
In [5]: letters[1:3]
Out[5]: [2, 3]
'''
列表解析
‘’‘
In [19]: numbers
Out[19]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
In [20]: f = filter(lambda x:x%2 == 0 ,numbers)
In [21]: list(map(lambda x:x**2, f))
Out[21]: [4, 16, 36, 64, 100]
’‘’
‘’‘
In [16]: [x**2 for x in numbers if x%2 == 0]
Out[16]: [4, 16, 36, 64, 100]
’‘’
字典解析
‘’‘
In [22]: d = {'a':1, 'b':2, 'c':3}
In [23]: {k:v**v for k, v in d.items()}
Out[23]: {'a': 1, 'b': 4, 'c': 27}
’‘’

元组拆包
‘’‘
 	t = ('hello', 'shiyanlou')
In [26]: a,b = t
In [27]: a
Out[27]: 'hello'
In [28]: b
Out[28]: 'shiyanlou'
In [29]: print('{}{}'.format(*t))
helloshiyanlou





