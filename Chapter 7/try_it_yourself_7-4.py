#Try it yourself 7-10:

vacation_dictionary = {}

while True:
    username = input('What is your name? ')
    vacation = input('Where do you want to go on vacation? ')

    vacation_dictionary[username] = vacation
    repeat = input('Would you like another person to respond? (yes / no) ')
    if repeat == 'no':
        break
print('___Poll Results___')
for name, response in vacation_dictionary.items():
    print(name.title() + ' would like to go to ' + response.title() + '!')
