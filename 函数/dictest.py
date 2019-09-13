#!/usr/bin/env python3
import sys

output_dict = {}

def handle_data(arg):
    arg = arg.split(':')
    a, b = arg
    output_dict[a] = b

def print_data(key, value):
    for key, value in output_dict:
        print("ID:{} Name:{}".format(key, value))

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    print(output_dict)

    for key in output_dict:
        print_data(key, output_dict[key])

