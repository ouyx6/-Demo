#!/usr/bin/env python3

import os
try:
	os.mkdir('/home/shiyanlou/syl')
except FileExistsError:
	print('the filename is exists')

try:
	os.mkdir('/home/shiyanlou/syl/A')
except FileExistsError:
	print('the filename is exists')

try:
	os.mkdir('/home/shiyanlou/syl/B')
except FileExistsError:
	print('the filename is exists')

try:
	os.mkdir('/home/shiyanlou/syl/C')
except FileExistsError:
	print('the filename is exists')

with open('/home/shiyanlou/syl/__init__.py','w') as f:
	f.close()
with open('/home/shiyanlou/syl/A/__init__.py','w') as f:
	f.close()
with open('/home/shiyanlou/syl/B/__init__.py','w') as f:
	f.close()
with open('/home/shiyanlou/syl/C/__init__.py','w') as f:
	f.close()

