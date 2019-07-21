def greet_user(username):
    """Display a simple greeting."""
    print('Hello ' + username.title() + '!')
    
greet_user('Kristin')

#Below - Positional arguments

def my_pets(pet_type, name):
    '''Display information about the howard pets'''
    print('\nI have a ' + pet_type + '.')
    print('And my '+ pet_type + 's name is ' + name.title() +'.')
my_pets('dog', 'lily')
#you can call a function as many times as you want, with different arguments
my_pets('bird', 'pierre')

#you can also use Keywork arguments so you do not mixup parameters 

my_pets(pet_type = 'rabbit', name = 'johnson')

def my_pets2(pet_type = 'dog', name):
    '''Display information about the howard pets'''
    print('\nI have a ' + pet_type + '.')
    print('And my '+ pet_type + 's name is ' + name.title() +'.')
my_pets('dog', 'lily')
