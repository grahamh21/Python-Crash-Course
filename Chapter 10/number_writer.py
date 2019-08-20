import json

numbers = [2,3,6,33, 100]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
