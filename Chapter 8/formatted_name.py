def formatted_name(first_name, last_name, middle_name = ''):
    """Return a name neatly formatted"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
namez = formatted_name('graham', 'howard', 'mckay')
print(namez)

def dictionary_name(first_nm, last_nm):
    '''defines a dictionary for a person'''
    person = {'first' : first_nm, 'last' : last_nm, }
    return person

identification = dictionary_name ('lily', 'howard')
print(identification)
