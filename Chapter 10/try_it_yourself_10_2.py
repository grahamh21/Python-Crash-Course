#Try it yourself 10-2: Learning C

filename = 'learning_python.txt'

with open(filename) as lp:
    py_list = lp.readlines()
    
    for line in py_list:
        print(line.replace('Python', 'java'))
