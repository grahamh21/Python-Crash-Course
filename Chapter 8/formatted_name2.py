def format_name(first_name, last_name):
    '''Obtain a formatted name'''
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('Please tell me your name! ')
    print("Press 'q' at any time to quit")
    f_name = input('First name: ')
    if f_name == 'q':
        break
        
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    formatted_name = format_name(f_name, l_name)    
    print('\nHello, ' + formatted_name + '!')

