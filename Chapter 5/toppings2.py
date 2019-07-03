toppings = ['pepperoni', 'cheese', 'potatoes']

#conditional test to see if toppings list is empty. Because the list has an
#item, it passes the conditional test as true, and runs through the 'for' loop. 
if toppings:
    for topping in toppings:
        if topping == 'cheese':
            print('vegan bitch')
        else:
            print('Adding ' + topping + ' to your pizza!')
    print('\nFinished with your pizza dough boy!')
else:
    print('Are you sure you want a plain pizza?')
