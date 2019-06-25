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

#Try_it_yourself 4-10
print('Try it yourself 4-10: Slices')

colors = ['red', 'blue', 'orange', 'green', 'yellow', 'black', 'white']
print('The first three items in the list are:')
print(colors[0:3])
print('The middle three items in the list are:')
print(colors[2:5])
print('The last three items in the list are:')
print(colors[-3:])

#Try_it_yourself 4-11
print('Try it yourself 4-11: pizzas')
my_pizzas = ['cheese', 'pepperoni', 'mushroom', 'meat', 'veggie', 'cream']
friend_pizza = my_pizzas[:]
print(my_pizzas)
print(friend_pizza)
my_pizzas.append('frank')
friend_pizza.append('charlie')
print('My favorite pizzas are:')
for pizzas in my_pizzas:
	print(pizzas)
print('\n')
for pizzas2 in friend_pizza:
	print(pizzas2)
