#Try it yourself 6-12:
favorite_numbers = {
    'greg': [35, 43, 9] , 'carol': [21, 211] ,
    'steve': [6,4556], 'jeremiah': [14],
    'lily' : [42069], 
    }
    
for names, numbers in favorite_numbers.items():
    if len(numbers)  > 1  :
        print(names.title() + "'s favorite number are: \n" +  str(numbers))
    elif len(numbers) <= 1 :
        print(names.title() + "'s favorite number is: \n" +  str(numbers))
