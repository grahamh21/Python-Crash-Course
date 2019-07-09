alien_1 = {'color': 'yellow', 'points' : 5}
print(alien_1['color'])
print(alien_1['points'])
# a dictionary is wrapped in braces {}, with a series of key-value pairs inside
#the braces.

#a key-value pair is a set of values associated with each other. When you provide
#a key, Python returns the value associated with that key. 

#every key is connected to its value by a colon, and individual key-value pairs
#are separated by commas. 
print(alien_1)
print('\n')
alien_1['x_position'] = 0
alien_1['y_position'] = 25

print(alien_1)

#can also start with empty dictionaries.

alien_2 = {}
alien_2['color'] = 'red'
alien_2['points'] = 10
print(alien_2)
