#!/usr/bin/env python3
from datetime import datetime

def log(func):
	def decorator(*args, **kwargs):
		print('Function' + func.__name__ + 'has been called at ' + datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
		return func(*args, **kwargs)
	return decorator

@log
def add(x, y):
	return x + y
add(1, 2)