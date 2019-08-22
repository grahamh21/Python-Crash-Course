#Try it yourself 10-12: Favorite Number Remembered

import json

def report_favorite_number():
    '''tells the favorite number if it exists'''
    try:
        with open('favorite_numbers2.txt') as number_object:
            favorite_numberz = json.load(number_object)
    except FileNotFoundError:
        print("You have not given us your favorite number yet!")
    else:
        print("Your favorite number is " + favorite_numberz)

def get_favorite_number():
    '''obtains a users favorite number if missing in report'''
    fav_num = input("What is your favorite number: ")
    filename = 'favorite_numbers2.txt'
    with open(filename, 'w') as num_obj:
        json.dump(fav_num, num_obj)
        print("We will remember this next time!")
    return fav_num
    

report_favorite_number()

