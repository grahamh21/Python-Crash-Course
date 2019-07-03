#Try it Yourself 5-10
current_users = ['George1', 'george2', 'george3', 'george4', 'george5', 'dino1']
new_users = ['george1', 'bob', 'claire', 'greg', 'lindsay', 'DINO1',]

current_users_lower = []
for user in current_users:
        current_users_lower.append(user.lower())
        
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('The username ' + new_user + ' is not available.')
    else:
        print('Yes! The username ' + new_user + ' is available!')
        
#Try it Yourself 5-11:oRDINAL nUMBERS

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')


