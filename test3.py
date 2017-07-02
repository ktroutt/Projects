"""This is a test of the emergency broadcast system"""
#Tip Calculator

"""def cube(number):
	return number ** 3

print cube(2)"""

def Tip(tits):
	return tits * .15

print Tip(100)

def Total(bill):
	Tax = bill * .08
	Tip = (bill + Tax) * .15
	All = bill +Tax +Tip
	return All 

print Total(100)