#!/usr/bin/env python3
import sys
import csv


test_filename = 'sys.argv[2]'

with open(test_filename,'r') as f:
	line_list = f.readline()
	line_dic = {}
	for i in line_list:
		i = i.split('=')
		line_dic[i[0]] = i[1]
#将test文件文件中的参数以字典方式输出，后一key：value 访问

user_filename = 'sys.argv[3]'

with open(user_filename, 'r') as u:
    u = list(csv.reader(u))
    user_dic = {}
    for j in u:
    	user_dic[u[0]] = u[1]

#for key, value in user_dic.items():

#user1 = Calculator(key,value)


# we need a data.csv to save rusult
with open('/tmp/gongzi.csv','w') as g:
	csv.writer(f).writerows(data)


class GetUser():
	#def __init__(self,id,pretax):
    #    self.id = id 
    #    self.pretax = pretax
    def get_user(self):
    		"""caculator other Cost"""
    	jishul = float(line_dic['JiShuL'])
    	jishuh = float(line_dic['JiShuH'])
		for self.id, self.pretax in user_dic.items():
			pretax = float(pretax)
			if pretax < jishul:
				pretax = jishul
			elif jishul < pretax <jishuh:
				pretax = pretax
			else:
				pretax = jishu
			FROG = pretax*0.08 + pretax*0.02 + pretax*0.005 + pretax*0.06
		
			pay_income = pretax - 5000 - FROG

			if pretax <= 5000:
				wage = pretax - FROG
				#print("??5000",wage)
			elif pay_income < 3000:
				pay_taxes = pay_income * 0.03 - 0
				#?????
				wage = pretax - FROG - pay_taxes
				#print("??5000",wage)
			elif pay_income > 3000 and pay_income <= 12000:
				pay_taxes = pay_income * 0.1 -210
				wage = pretax - FROG - pay_taxes
			elif pay_income > 12000 and pay_income <= 25000:
				pay_taxes = pay_income * 0.2 -1410
				wage = pretax - FROG - pay_taxes
			elif pay_income > 25000 and pay_income <= 35000:
				pay_taxes = pay_income * 0.25 - 2660
				wage = pretax - FROG - pay_taxes
			elif pay_income > 35000 and pay_income <= 55000:
				pay_taxes = pay_income * 0.3 - 4410
				wage = pretax - FROG - pay_taxes
			elif pay_income > 55000 and pay_income <= 80000:
				pay_taxes = pay_income * 0.35 - 7160
				wage = pretax - FROG - pay_taxes
			else:
				pay_taxes = pay_income * 0.45 - 15160
				wage = pretax - FROG - pay_taxes

			data = [self.id, pretax, FROG, pay_taxes, wage]

