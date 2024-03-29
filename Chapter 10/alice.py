filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #This counts the number of words in 'Alice in Wonderland'
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
title = "Alice in Wonderland"
title.split()
