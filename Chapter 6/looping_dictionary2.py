shapes = {'andrew' : 'square', 'sarah' : 'star', 'meghan': 'diamond', 'graham':
    'blunt', 'lily' : 'bone', 'murphy': 'wings',}

dogs = ['lily', 'murphy']
for name in shapes.keys():
 #   print(name.title())
# if key matches the dogs list, then the if statement prints out.     
    if name in dogs:
        print('Hello my favorite ' + name.title() + ', it is good to see you! I see ' +
        'your favorite shape is ' + shapes[name] + '!' )
    else:
        print('Hello ' + name.title() + ', your shape is ' + shapes[name] +
         ' and that is dumb!')
#line 10 - dictionary[variable(in this case name)] prints the value of the pair
# if instead we got rid of the dictionary[name], it would print the key.  

#This is using looping for every key-value pair in a dictionary as well as 
# an if else statement

if 'leo' not in shapes.keys():
    print('Leo, please say your favorite shape!')
