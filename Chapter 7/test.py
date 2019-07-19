unconfirmed_users = ['lily420', 'john316', 'mikeb']
confirmed_users = []

while unconfirmed_users:
#as long as unconfirmed_users is not empty
    current_user = unconfirmed_users.pop()

    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
