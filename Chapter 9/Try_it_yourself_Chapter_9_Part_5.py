#Try it yourself 9-6: Ice Cream Stand

class Restaurant():
    '''Defining a class called restaurant'''
    
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 23
        
# Any variable prefixed with self is available to every method in the class 
      
    def describe_restaurant(self):
        print('The name of the restaurant is ' 
            + self.restaurant_name.title() + '.')
        print('The food served is ' + self.cuisine_type + '.')
        print('People served: ' + str(self.number_served))
        
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')
        
    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers
        
    def increment_number_served(self, patrons):
        self.number_served += patrons
        
class IceCreamStand(Restaurant):
    '''An attempt at modeling a specific restaurant type.'''
    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initializing an ice cream restaurant.'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
        
    def display_flavors(self):
        '''a method to print the flavors in the ice cream shop.'''
        for flavor in self.flavors:
            print(flavor)

pittsford_dairy = IceCreamStand('pittsford dairy', 'ice cream')

pittsford_dairy.display_flavors()
print('\n')
#Try it yourself 9-7: Admin

class User():
    '''A way to model a user'''
    
    def __init__(self, first_name, last_name, job, birth_month, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.login_attempts = 0
        
        
    def describe_user(self):
        print('First Name: ' + self.first_name.title())
        print('Last Name: ' + self.last_name.title())
        print('Job: ' + self.job)
        print('Birth Month: ' + self.birth_month.title())
        print('Birth Year: ' + str(self.birth_year))
    
    
    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' 
        + self.last_name.title() + '.')

    def increment_login_attempts(self):
        '''increment login attempts by 1'''
        self.login_attempts += 1
    
    
    def reset_login_attempts(self):
        '''resets login attempts'''
        self.login_attempts = 0 #notice not 2 equal signs, only 1
        
class Admin(User):
    '''child class for Admins.'''
    
    def __init__(self, first_name, last_name, job, birth_month, birth_year):
        '''Initializing the Admin Child class.'''
        super().__init__(first_name, last_name, job, birth_month, birth_year)
        self.privileges = []
        
    def show_privileges(self):
        '''shows a list of the Admin privileges.'''
        for privilege in self.privileges:
            print('-' + privilege)
            
grahamh21 = Admin('graham', 'howard', 'admin', 'january', 1988)
grahamh21.privileges = ['can add post', 'can delete post', 'can ban user']
grahamh21.show_privileges()
        
