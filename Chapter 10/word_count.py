def count_words(filename):
    '''Count the approximate number of words in a file'''
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        with open('missing_files.txt', 'a') as miss_file:
            miss_file.write(filename)
        print(msg)
    else:
        #This counts the number of words in 'Alice in Wonderland'
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) +
         ' words.')
         
filenames = ['alice.txt', 'moby_dick.txt', 'john.txt', 'little_women.txt']      
for filename in filenames:
    count_words(filename)
