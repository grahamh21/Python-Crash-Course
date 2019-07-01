age = 9

if age < 5:
	print('too young bitch')
elif age < 19:
	print('5 bucks bitch')
else:
	print('AARP motherfucker')
#if both the if and elif test fails, then it prints the else block

print('\n')
age1 = 69
if age1 < 5:
	price = 0
elif age1 < 19:
	price = 5
else:
	price = 10
#notice the str(variable name)
print('The cost of the ride is $' + str(price) + '.')

age2 = 70
if age2 < 5:
	price = 0
elif age2 < 18:
	price = 5
elif age2 < 65:
	price = 10
else:
	price = 4.20
print('AARP bitch pays $' + str(price) +'.')	
#you can use as many elif blocks in your code as you like. 
#Python does not require an else block at the end of an if-elif chain. 
#Sometimes else is useful, sometimes, better to use elif
