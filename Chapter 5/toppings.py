requested_toppings = ['cheese', 'pepperoni', 'mushrooms']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping.upper() + ' to your order!')
print('\nYour pizza is finished!')
print('\n')

requested_toppings2 = ['cheese', 'pepperoni', 'mushrooms']
for requested_topping2 in requested_toppings2:
    if requested_topping2 == 'pepperoni':
        print('Sorry, we are out of ' + requested_topping2 + ' right now')
    else:
        print('Adding ' + requested_topping2 + ' to your pizza!')
print('\nYour pizza is finished being cooked!')
print('\n')
#to check if the list is empty, we start with an 'if' statement instead of a 'for' statement
toppings = ['pepperoni']

if toppings:
    for topping in toppings:
        print('Adding ' + topping + ' to your pizza!')
    print('\nFinished with your pizza dough boy!')
else:
    print('Are you sure you want a plain pizza?')
    
