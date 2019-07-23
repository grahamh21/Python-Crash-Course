#try it yourself 8-3: T-shirt

def make_shirt(size, text_message):
    '''function that shows the size and message on a t-shirt'''
    print('\nThe size of the t-shirt is ' + size + '.')
    print('The shirt will display ' + text_message + '.')
make_shirt('large', 'Bilbo Sw@ggIN$')

make_shirt(text_message = 'swag on', size = 'medium')

#try it yourself 8-4: T-shirt part deux

def make_shirt2(size = 'small', text_message = 'I love Python'):
    '''function that shows the size and message on a t-shirt'''
    print('\nThe size of the t-shirt is ' + size + '.')
    print('The shirt will display ' + text_message + '.')
make_shirt2()
make_shirt2(size = 'large')
make_shirt2(text_message = 'yolo')

#try it yourself 8-5: Cities

def describe_city(name, country = 'United States'):
    '''funciton that tells about cities and the country they are in'''
    print(name.title() + ' is in ' + country)
describe_city(name = 'boston')
describe_city(name = 'new york')
describe_city(name = 'london', country = 'england')
