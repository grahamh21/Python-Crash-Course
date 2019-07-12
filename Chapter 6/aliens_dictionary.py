aliens = []

for alien_number in range(31):
    new_alien = {'color': 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
print('...')
print('The total number of aliens is equal to: ' + str(alien_number))     
print('\n')
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
        
