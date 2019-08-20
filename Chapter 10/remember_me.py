import json

#load the user, if it has been stored previously.
#If not username exists, prompt for the username

def greet_user():
    '''Greet the user by name'''
    filename = 'username2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('We will remember you when you come back, ' + username + '!')
    else:
        print("Welcome back, " + username + "!")
greet_user()
# json.dump() function takes two arguments: a piece of data to store,
# and a file object it can use to store the data. 
