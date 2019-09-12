#!/usr/bin/env python3
import sys

pretax_pay = float(sys.argv[-1])
try:
	#
	lowest_weage = 5000
	axable_income = pretax_pay - lowest_weage

	if pretax_pay < lowest_weage:
	    weage = pretax_pay
	elif axable_income <= 3000:
		tax_annount = axable_income*0.03 - 0 
	elif axable_income > 3000 and axable_income <= 12000:
		tax_annount = axable_income*0.1 - 210
	elif axable_income > 12000 and axable_income <= 25000:
		tax_annount = axable_income*0.2 - 1410
	elif axable_income > 25000 and axable_income <= 35000:
		tax_annount = axable_income*0.25 - 2660
	elif axable_income > 35000 and axable_income <= 55000:
		tax_annount = axable_income*0.3 - 4410
	elif axable_income > 55000 and axable_income <= 80000:
		tax_annount = axable_income*0.35 - 7160
	else:
		tax_annount = axable_income*0.45 - 15160

	print("you must pay axable_income:{:.2f},tax_annount:{:.2f}".format(axable_income,tax_annount))
except ValueError:
	print("Parameter Error")
	
