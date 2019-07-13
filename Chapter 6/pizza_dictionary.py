pizza = {'crust' : 'thick', 'toppings' : ['cheese', 'pepperoni', 'mushrooms', 
'peppers']}

#summarizing the order
print('You ordered a ' + pizza['crust'] + 'crust pizza with the following ' +
 'toppings!')
for topping in pizza['toppings']:
    print(topping)
##############################################################################
    
favorite_toppings = { 'graham' : ['cheese', ],
    'leo' : ['spinach', 'mushrooms', 'feta'],
    'meghan' : ['sand', 'gravy', 'water'],
    'andrew' : ['leaves', 'lead', 'magnets'],
    }
for name, toppings in favorite_toppings.items():
    if len(toppings) > 1:
#by including the len() command, we refined the program to adjust grammar 
#to say favorite topping is instead of favorite toppings are
        print('\nThe favorite pizza toppings of ' + 
        str(name.title()) + ' are:')
    elif len(toppings) <= 1:
        print('\nThe favorite pizza topping of ' + 
        str(name.title()) + ' is:')
    for topping in toppings:
            print('\t' + topping)
