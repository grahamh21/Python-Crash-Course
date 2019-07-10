alien_2 = {'name' : 'bob', 'city' : 'rochester', 'age' : 23 , 'state': 'Ohio' }
print(alien_2)
print('\n')

del alien_2['age']
print(alien_2)

favorite_aliens = {
    'greg': 'jean',
    'carol': 'anthony',
    'bob': 'denise',
    'fletch': 'johnson',
    }

print('Carols favorite alien is ' + favorite_aliens['carol'].title() + '!')
