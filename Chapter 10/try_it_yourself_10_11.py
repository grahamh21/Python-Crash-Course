#Try it yourself 10-11: Favorite Number
import json


fav_num = input("What is your favorite number: ")
filename = 'favorite_numbers.txt'
with open(filename, 'w') as num_obj:
    json.dump(fav_num, num_obj)
print("We will remember your favorite number next time!")
