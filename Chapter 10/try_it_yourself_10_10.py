#Try it yourself 10-10: Common Words

filename = 'mars.txt'

with open (filename, encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents.lower().count('blow'))
    

