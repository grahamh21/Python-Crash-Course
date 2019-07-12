#Try it yourself 6-4:

glossary = {'slice': 'A specific group of item(s) in a list',
    'list comprehension': 'generate lists in one line of code',
    'range function' : 'use to generate a series of numbers',
    'string' : 'a series of characters',
    'concatenation': 'method of combining strings',
    'set' : 'similar to a list except that each item must be unique',
    'list' : 'collection of items in a particular order',
    'len()method' : 'can find the length of something using the len() function',
    'reverse()method' : 'used to reverse the original order of a list'
    }
    
for name in glossary.keys():
    print(name)
print('\n')
for value in glossary.values():
    print(value)
print('\n')
#Try it yourself 6-5:
rivers = {'egypt' : 'nile',
    'china' : 'yangtze', 
    'congo' : 'congo',
    }

for river in rivers.keys():
    print(river)
print('\n')
for river in rivers.values():
    print(river)
print('\n')

for country, water in rivers.items():
    print('the ' + water + ' river is in ' + country + '!')
#country is key, water is value -
print('\n')
#Try it yourself 6-6:
shapes = {'andrew' : 'square', 'sarah' : 'star', 'meghan': 'square', 'graham':
    'blunt', 'lily' : 'bone', 'murphy': 'wings', 'mark': 'diamind', }

players = ['sarah', 'mark', 'dave', 'thompkins', 'lily', 'lucy']

for names in players:
    if names in shapes.keys():
        print('Thank you ' + names + ' for taking our poll.')
    else:
        print('Hello ' + names +', would you please take our poll?')
#can use a for loop in the list, or in the dictionary.keys(), depends on
#what you want to poll.
