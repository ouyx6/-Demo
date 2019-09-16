#!/usr/bin/env python3
import sys

list1 = []
str1 = sys.argv[1:]

for i in range(1,len(str1)+1):
    str_i = sys.argv[i]
    str_f =str_i. split(':')
    list1.append(str_f)

dict1 = dict(list1)

for key,value in dict1.items():
	print("ID:{} NAME:{}".format(key,value))




