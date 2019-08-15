#Try it yourself 10-5: Programming Poll

filename = 'polling.txt'
question = 'Why do you like programming? '
question += "Enter 'stop' to end.\n"

with open(filename, 'a') as pole_file:
    while True:
        message = input(question)
        if message == 'stop':
            break
        else:
            pole_file.write('\n' + message)

