#!/usr/bin/env python3

def char_count(str_):
    char_list = set(str_)
    for char in char_list:
        print(char, str_.count(char))

if __name__ == '__main__':

    s = input("enter a string:")

    char_count(s)

