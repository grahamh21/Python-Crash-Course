suits = [ 'spades', 'clubs', 'hearts', 'diamonds' ]
#list starts with 0, so 1 is clubs, 3 is diamonds, etc
print(suits[2].title())
print(suits[0].upper())
#you can also use the string methods (.upper(), .title(), .rstrip(). etc on 
#any element in a list that you want.

friends = ['Jerry', 'Elaine', 'Kramer', 'George', 'Bob', 'Feldspar']
print(friends[4])
#you can select the last item in a list by choosing [-1]
print(friends[-1])
#this extends as well. [-2] is second last item in a list, [-3] is 3rd
#last etc.
declaration = 'The best character on friends is ' + friends[-2].upper() + '!'
print(declaration)


