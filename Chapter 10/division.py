# try:
    # print(5/0)
# except ZeroDivisionError:
    # print('You moron!')
    
#an exception object is an object that Python creates in response to a 
#situation where it can't do what it is asked.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number =='q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by zero!')
    else:
        print(answer)
