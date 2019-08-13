#Try it yourself 10-4: Guest Book

filename = 'guest_book.txt'

prompt = 'What is your name? '
prompt += "\nEnter 'quit' to end the program\n"

with open(filename, 'a') as gb:
    while True:
        name = input(prompt)
    
        if name == 'quit':
            break
        else:
            print('Greetings ' + name.title() + ', we are glad you are here!')
            gb.write('\n' + name)
            
            
