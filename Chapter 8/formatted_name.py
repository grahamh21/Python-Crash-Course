def formatted_name(first_name, last_name):
    """Return a name neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
namez = formatted_name('graham', 'howard')
print(namez)
