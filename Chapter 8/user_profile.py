def build_profile(first, last, **user_info):
	'''create a dictionary about a user'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
#function stops running when it reaches a return statement

user_profile = build_profile('albert', 'einstein',
							location= 'princeton', 
							field= 'physics')
user_profile2 = build_profile('graham', 'howard',
							career= 'IT', 
							status= 'cool guy')							
print(user_profile)
print('\n')
print(user_profile2)
