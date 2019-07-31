#Try it yourself 9-3: Users

class User():
    '''A way to model a user'''
    
    def __init__(self, first_name, last_name, job, birth_month, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.birth_month = birth_month
        self.birth_year = birth_year
        
    def describe_user(self):
        print('First Name: ' + self.first_name.title())
        print('Last Name: ' + self.last_name.title())
        print('Job: ' + self.job)
        print('Birth Month: ' + self.birth_month.title())
        print('Birth Year: ' + str(self.birth_year))
    
    
    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' 
        + self.last_name.title() + '.')


graham = User('graham', 'howard', 'network engineer', 'january', 1988)
pat = User('patrick', 'aldrich', 'network planner', 'january', 1988)
graham.greet_user()
print('\n')
graham.describe_user()
print('\n')

print('My friends name is ' + pat.first_name.title())
print('Here is some info about ' + pat.first_name)
pat.describe_user()
