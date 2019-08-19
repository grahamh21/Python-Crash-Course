#Try it yourself 10-7: Addition Calculator

#Already did that, so going to try the answer from the book for 10-6

try:
    x = input('First number: ')
    x = int(x)
    
    y = input('Second number: ')
    y = int(y)
    
    answer = x + y
except ValueError:
    print('number fuckhead')
else:
    print(answer)
