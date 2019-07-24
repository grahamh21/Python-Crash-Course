present_months = ['january', 'february', 'march', 'april', 'may']

past_months = []

print('present months are: ' + str(present_months))
print('past months are: ' + str(past_months))
while present_months:
    current_month = present_months.pop()
    past_months.append(current_month)
    
print('present months are: ' + str(present_months))
print('\npast months are: ' + str(past_months))

#The above is a while loop, but functions can make this more efficient. 

