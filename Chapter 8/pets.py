def my_pets2(name, pet_type = 'dog'):
    '''Display information about the howard pets'''
    print('\nI have a ' + pet_type + '.')
    print('And my '+ pet_type + 's name is ' + name.title() +'.')
my_pets2( name = 'lily')

#when using default values, you have to match the argument to the parameter. 
#default values have to come after non-default values. 

def my_pets3(name, pet_type = 'dog'):
    '''Display information about the howard pets'''
    print('\nI have a ' + pet_type + '.')
    print('And my '+ pet_type + 's name is ' + name.title() +'.')
my_pets3( name = 'swag', pet_type = 'marmot')

#above, default values is ignored b/c an explicit argument type is provided. 

#Equivalent Function calls
#all are the same

my_pets3('lily')
my_pets3(name = 'lily', pet_type = 'dog')

#changing it to hamster cat named dave

my_pets3('dave', 'cat')
my_pets3(name = 'dave', pet_type = 'cat')
my_pets3(pet_type = 'cat', name = 'dave')
