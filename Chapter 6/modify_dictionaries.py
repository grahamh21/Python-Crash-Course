alien_1 = {'color': 'yellow'}
print('The alien is ' + alien_1['color'] + '!\n')

alien_1['color'] = 'red'
print('The alien is now ' + alien_1['color'] + '!\n')

#===========================================================
alien_0 = {'x_position' : 0 , 'y_position' : 25 , 'speed' : 'slow' }
print(alien_0)
print('\n')

print('Original x-position: ' + str(alien_0['x_position']))
print('Original y-position: ' + str(alien_0['y_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#adjusting the x_position of the alient
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('\n')
print('The new x-position of the alien is: ' + str(alien_0['x_position']))  

alien_2 = {'name' : 'bob', 'city' : 'rochester', 'age' : 23 , 'state': 'Ohio' }
print(alien_2)
