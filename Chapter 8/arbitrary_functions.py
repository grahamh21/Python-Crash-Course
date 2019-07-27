def make_pizza(*toppings):
	'''print the list of toppings'''
	print('The following toppings are being added:\n')
	for topping in toppings:
		print('- ' + topping)
	
make_pizza('pepperoni')
make_pizza('pepperoni', 'cheese', 'mushrooms')


def make_cake(size, *toppings):
	'''describes cake size'''
	print('Making a ' + str(size) + ' inch cake')
	print('with the following ingredients:')
	for topping in toppings:
		print('- ' + topping)
make_cake(10, 'apple', 'caramel', 'cheese')
