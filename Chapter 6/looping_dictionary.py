fish_1 = {'color': 'orange', 'age' : 'thirteen', 'name' : 'garcon', 
    'type' : 'angel'}

for key, value in fish_1.items():
    print('\nKey: ' +  key)
    print('Value: ' + value)
    
# Line 4 - key and value are two variables that we created. the .items() method
#at the end of fish_1 in line 4 returns the key-value pairs. 
#we could easily rename them whatever we want, however using key&value for simpleness.

shapes = {'andrew' : 'square', 'sarah' : 'star', 'meghan': 'diamond', 'graham':
    'blunt', 'lily' : 'bone', 'murphy': 'wings',}
    
#as it works through each pair below, store the key in the variable name, and
#the value in the variable shape.     
for name, shape in shapes.items():
    print(name.title() + "'s favorite shape is " + shape)
#here, we rename the variables to name and shape. For every name in the loop,
#print their favorite shape. 


#dictionary.items() goes through each key-value pair in a dictionary. 
#if we only want the keys, or only want the values, can do dictionary.keys() 
# and dictionary.values()

print('Everyone that submitted a favorite shape is:')
print(shapes.keys())
print('\n')
for name in shapes.keys():
    print(name.title())
#also notice the different ways it prints the dictionaries. 
#print(shapes.keys()) posts in one line, while the for loop prints one and then
#prints another on a new line.
 
dogs = ['lily', 'murphy']

for nam
