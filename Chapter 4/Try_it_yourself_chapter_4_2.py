#Try_it_yourself 4-7
print('Try it yourself 4-7')
threes = list(range(3,31,3))
for three in threes:
	print(three)

#Try_it_yourself 4-8
print('Try it yourself 4-8\n')

cubes = []
for cube in range(1,11):
	cubes.append(cube**3)
print(cubes)

#Try_it_yourself 4-9
print('Try it yourself 4-9')
#list comprehension
cubed = [quark**3 for quark in range(1,11)]
print(cubed)

#range() function generates a series of numbers
#from there, you can manipulate it in a list comprehension or other ways
