#Try it yourself 5-1
print('Try it yourself: 5-1')

#1 - False statement due to capitalization 
food = 'German'
print('Am I hungry for == "german" ? I predict false')
print(food == 'german')
print('\n')
#2 - now true because food.lower == german
print(food.lower() == 'german')
print('\n')
#3 - False statement due to different variable
lovers = ['carol', 'sj', 'lauren', 'almul', 'ri']
print(lovers == 'wine')
print('\n')
#4 - True statement due to same variable - include 'in' keyword - 
print('sj' in lovers)
print('\n')
#5 - Not equal (!=) - should be true
print('booze' != lovers)
print('\n')
#6 - variable not in lovers
print('cheese' not in lovers)
print('\n')
#7 - False statement - string in variable
print('lauren' not in lovers)


#Try it yourself 5-2
print('Try it yourself: 5-2')
# 1 & 2: Tests for equality and inequality w/ strings 
#!!!!german tests above - equality, inequality, and lower() function
# 3: Numerical tests involing equality and inequality, greater than and less than, etc
# 4: Tests using the 'and' keyword and the 'or' keyword
# 5 & 6: Test where an item is in a list or not in a list

# 4: 
if 'carol' not in lovers and 'john' not in lovers:
    print('boobs!')
#indented else did not work, had to put it at the bottom
else:
    print('no!')
lovers = ['carol', 'sj', 'lauren', 'almul', 'ri']
#trying to include loop - 
#define lovers = 5 names
#for every name in lovers, check to see if its almul,
for lover in lovers:
    if lover == 'almul':
        print('oil!')
else: 
    if lover != 'almul':
        print('flat')
