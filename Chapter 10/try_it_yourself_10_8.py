#Try it yourself 10-8: Cats and dogs

filename = 'dogs.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
        
except FileNotFoundError:
    print('The file ' + filename + ' does not exist.')
    
else:
    print(contents)
        

