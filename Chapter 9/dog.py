class Dog():
    '''Simple dog class'''
    
    def __init__(self, name, age):
        '''Initialize name and age attributes'''
        self.name = name
        self.age = age
        
    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(self.name.title() + ' is now sitting.')
        
    def roll_over(self):
        '''simulate a dog rolling over in response to a command'''
        print(self.name.title() + ' rolled over!')

my_dog = Dog('lily', 6)

print('My dogs name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old!')
print('\n')
old_dog = Dog('murphy', 11)

print('My dogs name is ' + old_dog.name.title() + '.')
print('My dog is ' + str(old_dog.age) + ' years old!')
