shapes = {'andrew' : 'square', 'sarah' : 'star', 'meghan': 'diamond', 'graham':
    'blunt', 'lily' : 'bone', 'murphy': 'wings',}

for name in sorted(shapes.keys()):
    print(name.title() + ', thank you for taking our poll!')
print('\n')
for shape in sorted(shapes.values()):
    print(shape.upper() + ' was a response!')
