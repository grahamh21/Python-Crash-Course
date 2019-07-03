#Try It Yourself - 5:6

age = 22

if age < 2:
    print('you are a baby!')
elif age < 4:
    print('you are a toddler')
elif age < 13:
    print('You are a KID')
elif age < 20:
    print('You are a teenager!')
elif age < 65:
    print('You are an Adult!')
elif age >= 65:
    print('You are an Elder!')

#Try It Yourself - 5:7

favorite_fruits = ['Oranges', 'strawberries', 'grapes']

if 'Oranges' in favorite_fruits:
    print('orange boy')
if 'apples' in favorite_fruits:
    print('gross')
if 'grapes' in favorite_fruits:
    print('grapes') 

#Try It Yourself - 5:8 Hello Admin
#using tuples instead of lists, hence the () instead of [] 
usernames = ('admin', 'lendog50', 'greg', 'yoloswaggins', '420blaze')

for username in usernames:
    if username == 'admin':
        print('Hello admin! Would you like to see a status report?')
    else:
        print('Hello ' + username + '. Welcome to the website!')
    
