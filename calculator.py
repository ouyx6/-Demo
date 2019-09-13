#!/usr/bin/env python3
import sys
employee_wage = {}
def get_wage():
	"""make the input to a employee_wage dict"""
	for str_pretax_pays in sys.argv[1:]:
		#print(str_pretax_pays)
		str_pretax_pay1 = str_pretax_pays.split(':')
		a, b = str_pretax_pay1
		employee_wage[a] = b
	return employee_wage

def caculator_wage():
	"""caculator other Cost"""
	for num, pretax in employee_wage.items():
		pretax = float(pretax)#字典中提取的为字符串，需将起改为浮点数
		print(type(pretax), pretax)
		FROG = pretax*0.08 + pretax*0.02 + pretax*0.005 + pretax*0.06
		#print("五险一金：",FROG)
		pay_income = pretax - 5000 - FROG
		#应缴纳所得税金额
		#print("纳税金额：", pay_income)
		if pretax <= 5000:
			wage = pretax - FROG
			#print("减税5000",wage)
		elif pay_income < 3000:
			pay_taxes = pay_income * 0.03 - 0
			#需纳税金额
			wage = pretax - FROG - pay_taxes
			#print("减税5000",wage)
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

		#print("工资：", wage)


		employee_wage[num] = wage

	print(employee_wage)

def print_wage():
	"""print weget"""
	for i, j in employee_wage.items():
		print("{}:{:.2f}".format(i,j))

if __name__ == '__main__':
	get_wage()
	caculator_wage()
	print_wage()



