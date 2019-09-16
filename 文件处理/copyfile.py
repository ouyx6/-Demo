#!/usr/bin/env python3

#with open('/home/shiyanlou/shiyanlou.txt') as f:
#    with open('/home/shiyanlou/shiyanlou_copy.txt','w')as c_f:
with open('shiyanlou.txt') as f, open('shiyanlou_copy.txt', 'w') as c_f:
        line_read = []
        for line in f.readlines():
        	#print(line)
        	line = line.strip('\n')
        	#print(line)
        	line_read.append(line)

        print(line_read)


        for i, j in enumerate(line_read):
        	print('{} {}'.format(i+1, j))
        	c_f.write('{} {}'.format(i+1,j)+'\n')
            



