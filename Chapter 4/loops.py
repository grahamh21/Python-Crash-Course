suckers = ['carol', 'anthony', 'greg']
for sucker in suckers:
	print(sucker.upper() + ' is a bad muhfuh!')
#every indented line following the 'for loop' is considered inside the loop
	print('Beeooottch ' + sucker.upper() + '\n')
#added the print( string '\n') to give it more space

print('Thank you to all the Jabberwockies!\n')

dogs = ['lily', 'otis', 'tae', 'murphy']
for dog in dogs:
	print(dog)

for value in range(1,30):
	print(value)
#python never prints the last number, so this will print 1-29
#need to add +1 to print the final number (ie 1-31)

numbers = list(range(1,16))
print(numbers)
#convert numbers to a range with list(range(x, y))
#can also skip by 2 or 3 etc.
odd_numbers = list(range(1,12,2))
print(odd_numbers)

squares = []
for square in range(1,10):
	squared = square**2
	squares.append(squared)
print(squares)
#this is not a bad way to write the code, but can be tighter

circles = []
for circle in range(1,11):
	circles.append(circle**2)
print(circles)
#empty list varible = circles
#circle variable = range 1-10 
#we append every number in circle range, and square it, then append
