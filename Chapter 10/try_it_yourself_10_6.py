#Try it yourself 10-6:Addition

prompt = 'Add two numbers together to get their sum'
prompt += "\nEnter 'stop' to quit"

while True:
    print(prompt)
    first_number = input('\nFirst number: ')
    if first_number == 'stop':
        break
    second_number = input ('Second number: ')
    if second_number == 'stop':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number instead of a letter moron")
    else:
        print(answer)
            
    
