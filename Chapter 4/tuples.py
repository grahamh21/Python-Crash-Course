sizes = (12, 15,20)
print(sizes[0])
print(sizes[1])

print(sizes)
#sizes[0] = 13 - once a tuple is assigned, you cannot change the values

print('The original sizes are:')
print(sizes)

for size in sizes:
	print(size)
sizes = (11, 13, 14)
print('\n')
for size in sizes:
	print(size)
#although we cannot change the values in the tuple, we can overright the entire variable
print('\n')
buffet = ( 'chicken', 'beef', 'cheese', 'meat', 'pork' )
for food in buffet:
	print(food)
#buffet[1] = 'cow'
print('\n')
buffet = ( 'beer', 'water', 'cheese', 'meat', 'pork' )
for food in buffet:
	print(food)
