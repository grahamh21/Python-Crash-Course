#Try it yourself 7-1:
rental_car = 'what kind of car would you like?'

message = input(rental_car)

print('Let me see if I can find you a ' + message + '!')

#Try it yourself 7-2:

seating = input('How many people are in your party?')
seating = int(seating)

if seating <= 8 :
    print('Right this way for your table')
else:
    print('You will have to wait for a table')

#Try it yourself 7-3:

question = 'Please tell me a number and I will tell you if it divides by 10\n'
question += 'Please enter a number: ' 

answer = input(question)
answer = int(answer)

if answer % 10 == 0:
    print('The number ' + str(answer) + ' is divisible by 10!')
else:
    print('The number ' + str(answer) + ' is not divisible by 10!')
