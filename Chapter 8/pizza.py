def make_pizza(size, *toppings):
	'''describes pizza size and toppings'''
	print('Making a ' + str(size) + ' inch pizza')
	print('with the following ingredients:')
	for topping in toppings:
		print('- ' + topping)
