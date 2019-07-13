#Try it yourself 6-7:
person1 = {'name': 'kristy', 'surname': 'love', 'age':30 , 'city':'rochester',
    'state': 'new york', }
person2 = {'name': 'John', 'surname': 'Macenroe', 'age':69 , 'city':'Paris',
    'state': 'France', }
person3 = {'name': 'Jason', 'surname': 'Bourne', 'age':21 , 'city':'Madrid',
    'state': 'Spain', }
people = [person1, person2, person3]

for person in people:
    print(person)
print('\n')
#Try it yourself 6-8:
lily = {'animal' : 'dog', 'owner' : 'graham',}
pierre = { 'animal' : 'bird', 'owner' : 'virginia',}
franklin = { 'animal' : 'puppet', 'owner' : 'gob', }
pets = [lily, pierre, franklin]
for pet in pets:
    print(pet)
#Try it yourself 6-9:
print('\n')

favorite_places = {'graham' : ['boston', 'spain', 'france'],
    'jay' : ['portugal', 'lisbon', 'madrid'], 
    'dennis' : ['provincetown', 'newport', ]
    }
for name, places in favorite_places.items():
    print('My name is ' + name + ', and my favorite places are:')
    for place in places:
        print('\t' + place)
#for loop for variables name & place
#Try it yourself 6-10:
