#Try it yourself_8-12: Sandwiches

def sandwiches1(*toppings):
	print('Here is your sandwich ingredients: ')
	for topping in toppings:
		print('--' + str(topping))
sandwiches1('cheese')
sandwiches1('peppers', 'olives',)
sandwiches1('cheese', 'grain', 'mushrooms')

#Try it yourself_8-13: User Profile

def build_profile(first, last, **user_info):
	'''create a dictionary about a user'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile


user_profile2 = build_profile('graham', 'howard',
							career= 'IT', 
							status= 'cool guy')	
print(user_profile2)

#Try it yourself_8-14: Cars

def cars(manufacturer, model, **car_info):
	'''stores a dictionary about a car'''
	information = {}
	information['car manufacturer'] = manufacturer
	information['car model'] = model
	for key, value in car_info.items():
		information[key] = value
	return information

car1 = cars('bmw', 'm5', color='red', sound_system='bose')

print(car1)
