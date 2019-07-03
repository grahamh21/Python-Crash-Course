available_toppings = ['extra cheese', 'mushrooms', 'pepperoni', 'anchovies', 
'peppers', 'onions', 'sausage']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + ' to your pizza!')
    else:
        print('Sorry, we do not have ' + requested_topping + ' available!')
print('\nFinished cooking your pizza!')
