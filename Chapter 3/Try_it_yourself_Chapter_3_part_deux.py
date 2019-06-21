#Try It Yourself 3-8
print('Try It yourself 3-8')
vacations = [ 'italy', 'germany', 'france', 'portland', 'patagonia']
print(vacations)
print(sorted(vacations))
print(vacations)
print (sorted(vacations, reverse=True))
print(vacations)
vacations.reverse()
print(vacations)
vacations.reverse()
print(vacations)
vacations.sort()
print(vacations)
vacations.sort(reverse=True)
print(vacations)

#Try It Yourself 3-10
print('\nTry It yourself 3-10')
lovers = ['liz', 'colleen', 'grace', 'lisa', 'krista', 'cassandra', 'kristin',]
#individual values from a list variable[x]
print(lovers[3])
# modifying element in a list varible[x] = 'new value'
lovers[4] = 'hand'
print(lovers)
#appending elements to a list 
lovers.append('krista')
print(lovers)
#inserting elements in a list - variable.insert ( #, 'string')
#!!!!append adds to end, insert adds to a specific position
lovers.insert( 5, 'claire')
print(lovers)
# removing elements from a list with del- del variable[#]
del lovers[5]
print(lovers)
#del removes permanantly, pop moves to another temp list you can use again
#removing elements with pop - 
ex_lovers = lovers.pop()
print(ex_lovers)
ex_lovers = lovers.pop(4)
print(ex_lovers)
print(lovers)
#removing item by value - sometimes won't know position of the value, so can remove by value of item
lovers.remove ('liz')
print(lovers)
#can sort list permanantly or temporarily - varible.sort does permanantly
lovers.sort()
print(lovers)
#sorted.variable does not affect permanantly
print(sorted(lovers,reverse=True))
print(lovers)
#reverse method changes the order of a list permanantly
lovers.reverse()
print(lovers)
#can find length of the list quickly using the len() function
print('There are ' + str(len(lovers)) )
print( str(len(lovers)))
#last item in a list - variable[-1]
print(lovers[-2])


