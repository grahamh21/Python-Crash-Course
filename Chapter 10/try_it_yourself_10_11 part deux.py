#Try it yourself 10-11: Favorite Number part 2

import json

filename = 'favorite_numbers.txt'

with open(filename) as number_object:
    favorite_numberz = json.load(number_object)
    print("Your favorite number is " + favorite_numberz)
