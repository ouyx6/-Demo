#!/usr/bin/env python3
import sys
import csv

class Calculator():
	def __init__(self,test_filename,user_filename):
		self.test_filename = test_filename
		self.user_filename = user_filename


	def get_test(self):
		'''定义一个获取test文件数据的函数，访问一个字符串字典'''
		#test_filename = 'sys.argv[2]'
		with open(self.test_filename,'r') as f:
			line_list = f.readlines()
			self.line_dic = {}
			for i in line_list:
				i = i.strip()
				i = i.split('=')
				#print(i)
				self.line_dic[i[0]] = i[1]
		print(self.line_dic)


		return self.line_dic
#将test文件文件中的参数以字典方式输出，后一key：value 访问

	def get_user(self):
		'''定义一个获取user文件数据的函数，返回以个包含id，pretax'''

		#user_filename = 'sys.argv[3]'

		with open(self.user_filename, 'r') as u:
		    user_list = list(csv.reader(u))
		    #print(user_list)
		    self.user_dic = {}
		    for j in user_list:
		    	self.user_dic[j[0]] = j[1]

		print(self.user_dic)
		return self.user_dic
#for key, value in user_dic.items():
#user1 = Calculator(key,value)
# we need a data.csv to save rusult
#with open('/tmp/gongzi.csv','w') as g:
#	csv.writer(f).writerows(data)
    def caculator_wage(self):
    	"""caculator other Cost"""
    	jishul = float(self.line_dic['JiShuL'])
    	jishuh = float(self.line_dic['JiShuH'])
		for self.id, self.pretax in self.user_dic.items():
			self.pretax = float(pretax)#将税前工资由字典中的字符串变为浮点数
			if self.pretax < jishul:
				pretax1 = jishul
			elif jishul < pretax <jishuh:
				pretax1 = self.pretax
			else:
				pretax1 = jishu

			#将税前工资与 基数高 和 低 做比较，选出计算社保的基数。
			FROG = pretax1*0.08 + pretax1*0.02 + pretax1*0.005 + pretax1*0.06
			#五险一金
		
			pay_income = self.pretax - 5000 - FROG
			#纳税基数

			#wage:工资， pay_taxes:个税金额

			if self.pretax <= 5000:
				wage = self.pretax - FROG
			elif pay_income < 3000:
				pay_taxes = pay_income * 0.03 - 0
				wage = self.pretax - FROG - pay_taxes
			elif pay_income > 3000 and pay_income <= 12000:
				pay_taxes = pay_income * 0.1 -210
				wage = self.pretax - FROG - pay_taxes
			elif pay_income > 12000 and pay_income <= 25000:
				pay_taxes = pay_income * 0.2 -1410
				wage = self.pretax - FROG - pay_taxes
			elif pay_income > 25000 and pay_income <= 35000:
				pay_taxes = pay_income * 0.25 - 2660
				wage = self.pretax - FROG - pay_taxes
			elif pay_income > 35000 and pay_income <= 55000:
				pay_taxes = pay_income * 0.3 - 4410
				wage = self.pretax - FROG - pay_taxes
			elif pay_income > 55000 and pay_income <= 80000:
				pay_taxes = pay_income * 0.35 - 7160
				wage = self.pretax - FROG - pay_taxes
			else:
				pay_taxes = pay_income * 0.45 - 15160
				wage = self.pretax - FROG - pay_taxes

			data = [self.id, self.pretax, FROG, pay_taxes, wage]

			with open('/tmp/gongzi.csv','w') as g:
				csv.writer(f).writerows(data)



if __name__ == '__main__':
	caculator = Calculator('/home/ouyx/test.cfg','/home/ouyx/user.csv')
	
	caculator.get_test()
	caculator.get_user()
	
