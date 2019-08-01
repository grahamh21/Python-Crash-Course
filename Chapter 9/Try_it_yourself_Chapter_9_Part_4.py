#Try it yourself 9-5: Login Attempts

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
        
grahamh = User('graham', 'howard', 'network engineer', 'january', 1988,)
grahamh.increment_login_attempts()
grahamh.increment_login_attempts()
grahamh.increment_login_attempts()
grahamh.increment_login_attempts()
grahamh.increment_login_attempts()
print(str(grahamh.login_attempts))
grahamh.reset_login_attempts()
print(str(grahamh.login_attempts))
