from user_module import User

class Privileges():
    '''Defining class to be used as an attribute.'''
    
    def __init__(self, privileges=[]):
        '''Initializing the privileges class.'''
        self.privileges = privileges
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        '''shows a list of the Admin privileges.'''
        for privilege in self.privileges:
            print('-' + privilege) 

class Admin(User):
    '''child class for Admins.'''
    
    def __init__(self, first_name, last_name, job, birth_month, birth_year):
        '''Initializing the Admin Child class.'''
        super().__init__(first_name, last_name, job, birth_month, birth_year)
        
        self.privileges = Privileges()
