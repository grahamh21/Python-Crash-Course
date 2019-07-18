#Try it yourself 7-4:
question = 'Please enter a pizza topping and we will confirm the topping\n'
question += 'Enter "quit" to end the order: '


while True:
    message = input(question)
    if message == 'quit':
        break
    else:
        print('We will add ' + message + ' to your pizza!')
#created an infinite loop above by putting message = input(question) above
#the while loop. By putting the message = input(question) inside the while
#loop, we break the infiniite loop. 

#Try it yourself 7-5:

prices = input('What is your age? ')
#User inputs a string, we convert it to an integer
prices = int(prices)


#set flag equal to true - 
if prices <= 3:
        print('Your ticket is free!')
elif prices <= 12:
        print('Your ticket costs 10$ ')
else:
        print('Your ticket costs 15$')
#Try it yourself 7-6:
questionz = 'Please enter a pizza topping and we will confirm the topping\n'
questionz += 'Enter "quit" to end the order: '

while True:
    message = input(questionz)
    if message == 'quit':
        break
    else:
        print('We will add ' + message + ' to your pizza!')

questiona = 'Please enter a pizza topping and we will confirm the topping\n'
questiona += 'Enter "stop" to end the order: '

active = True

while active:
    toppings = input(questiona)
    if toppings == 'stop':
        active = False
    else:
        print('We are adding ' + toppings + ' to your pie!')

lazer = 'Please enter a pizza topping and we will confirm the topping\n'
lazer += 'Enter "pow" to end the order: '

gun = ''
while gun != 'pow':
    gun = input(lazer)
    print('We are adding ' + gun + ' to your gun!')



#Try it yourself 7-7: Infinite loop
question = 'Please enter a pizza topping and we will confirm the topping\n'
question += 'Enter "quit" to end the order: '

message = input(question)
while True:
    
    if message == 'quit':
        break
    else:
        print('We will add ' + message + ' to your pizza!')

