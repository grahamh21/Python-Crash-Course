zorg = input('Please enter a number to determine if even or odd: ')
zorg = int(zorg)

if zorg % 2 == 0:
    print('The number ' + str(zorg) + ' is Even!')
else:
    print('The number ' + str(zorg) + ' is Odd!')
#This test determines if a number is even or odd and tells you the number  

state = 'What is the name of a state you have visited this year? \n'
state += "Enter 'stop' to end the program."

flag = True

while flag:
    message = input(state)
    if message == 'stop':
        flag = False
    else:
        print('Thats cool. Did you enjoy visiting ' + message.title() + '?')

#state variable at the top should not be an input() command. 
#set the input() as we declare the variable message. 


cigar = 'What is your favorite color of jeans? \n'
cigar += "Enter 'buttstuff' to quit the program."

while True:
    answer = input(cigar)
    if answer == 'buttstuff':
        break
    else:
        print('The jean material ' + answer.upper() + ' is dumb rtard!')
