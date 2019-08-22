import json

#load the user, if it has been stored previously.
#If not username exists, prompt for the username

def get_stored_username():
    '''get stored username if available'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''prompt for a new username'''
    username = input("What is your name? \n")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    '''Greet the user by name'''
    username = get_stored_username()
    if username:
        print()
        right_user = input("Are you " + username + "? \nEnter 'yes' or 'no'\n")
        if right_user == 'yes':
            print("Welcome back, " + username.title() + "!")
        else:
            username = get_new_username()
            print('We will remember you when you come back, ' + username + '!')
    else:
        username = get_new_username()
        print('We will remember you when you come back, ' + username + '!')
        
greet_user()

# json.dump() function takes two arguments: a piece of data to store,
# and a file object it can use to store the data. 
