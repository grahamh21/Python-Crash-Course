#Try it yourself 10-1: Learning Python

filename = 'learning_python.txt'

#looping over the file object
with open(filename) as file_object:
    lines = file_object.readlines()
    
    for line in lines:
        print(line.strip())
        
print('\n')
#reading the entire file
with open(filename) as file_object2:
    lines2 = file_object2.read()
    
    print(lines2)

#working with a list outside of the with open() block
with open(filename) as file_object3:
    lines3 = file_object3.readlines()

python_list = ''

for line in lines3:
    python_list += line
    
print(python_list)
