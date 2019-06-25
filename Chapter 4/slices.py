pens = ['gl', 'cross', 'bic', 'highlighter', 'quarks', 'adams', 'clints', 'splintz', 'bonez']
print(pens[0:2])
#similar to range() function, have to increase by one for the number ie
# range(1,11) specifies 1 through 10
print(pens[2:5])
#can specifiy start and stop using the slice portion 

#if you omit the first number, python starts at the beginning of the list
print(pens[:3])
#something similar happens if you don't include a second number
print(pens[3:])

#this also works for negative numbers as well
print(pens[0:-3])

print('Here are my favorite pen types:')
for pen in pens[:4]:
	print(pen.title())
#using slice to loop only a portion of the items on the list

cars = ['dodge', 'buick', 'ram', 'chevy', 'bmw']
trucks = cars[:]

print('My favorite cars are:')
print(cars)

print('Trucks are also:')
print(trucks)

cars.append('copter')
trucks.append('flash gordon')
print(cars)
print(trucks)
