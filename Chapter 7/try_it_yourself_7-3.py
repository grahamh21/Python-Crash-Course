#Try it yourself 7-8:
sandwich_orders = ['tuna', 'cuban', 'reuben', 'blt',]
finished_orders = []

#moving items from one list to another

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I have made your ' + current_sandwich + ' sandwich!')
    finished_orders.append(current_sandwich)
print('---The following sandwiches have been made:---') 
for sandwich in finished_orders:
    print(sandwich)
#Try it yourself 7-9:
print('\n')
sandwich_orders2 = ['tuna','pastrami', 'cuban', 'reuben', 'pastrami', 'blt',
    'pastrami']
finished_orders2 = []

print(sandwich_orders2)
print('\n')
print('The Deli has run out of Pastrami fools')

while 'pastrami' in sandwich_orders2:
    sandwich_orders2.remove('pastrami')
while sandwich_orders2:
    hamwich = sandwich_orders2.pop()
    finished_orders2.append(hamwich)
print(finished_orders2)
#Try it yourself 7-10:

question = 'Where would you go on vacation? '
question += input('enter "stop" to quit. ')

print(question)
