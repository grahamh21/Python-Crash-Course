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
favorite_numbers = {
    'greg': [35, 43] , 'carol': [21, 211] ,
    'steve': [6,4556], 'jeremiah': 14,
    'lily' : 42069, 
    }
    
for names, numbers in favorite_numbers.items():
    if len(str(numbers))  > 1  :
        print(names.title() + "'s favorite number are: \n" +  str(numbers))
    elif len(str(numbers)) <= 1 :
        print(names.title() + "'s favorite number is: \n" +  str(numbers))
    

#Try it yourself 6-11:

cities = {'boston' : {'country' : 'usa', 'population' : 'one million' ,
     'fact': 'tea party' }, 
    'london' : {'country' : 'england', 'population' : 'five million', 
    'fact' : 'bad teeth'}, 
    'madrid' : {'country' : 'spain', 'population' : 'two million', 
    'fact' : 'cool place'}
    }
for place, facts in cities.items():
    print('City: ' + place.title())
    print('\tCountry: ' + facts['country'])
    print('\tPopulation: ' + facts['population'])
    print('\tFact: ' + facts['fact'])
