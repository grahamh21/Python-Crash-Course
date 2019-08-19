#Try it yourself 10-9: Silent Cats and Dogs

filename = 'dogz.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
        
except FileNotFoundError:
    pass
    
else:
    print(contents)
        
