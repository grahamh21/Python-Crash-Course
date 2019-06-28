ladies = ['grace', 'colleen', 'lisa', 'carla', 'kristin', 'krista']
for lady in ladies:
    if lady == 'lisa':
        print(lady.upper())
    else:
        print(lady.title())

print('\n')
boobs = 'huge'
if boobs != 'small':
    print('Boooooo!')
# this if statement is true - boobs is not equal to huge 
# most of the time, can test for equality, but can also test for inequality
print('\n')
dice = '6'
if dice != 3:
    print('No dice!')


losers = ['nog', 'nd', 'dave', 'ladybug']
user = 'johnson'

if user not in losers:
    print(user.title() + ', you can post here!')
    
