#Try it yourself 10-3: Guest

filename = 'guest.txt'

first_name = input('What is your name? ')

with open('guest.txt', 'w') as guest_file:
    guest_file.write(first_name)
