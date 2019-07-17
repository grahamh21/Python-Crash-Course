check_numbers = input("Tell me a number and I'll say if its even or odd: ")
check_numbers = int(check_numbers)

if check_numbers % 2 == 0 :
    print('\nThe number you entered is even!')
else:
    print('\nThe number you entered is odd!')

current_numbers = 1
while current_numbers <= 5:
    print(current_numbers)
    current_numbers += 1
print('\n')
odd_numbers = 0

while odd_numbers < 10:
    odd_numbers += 1
    if odd_numbers % 2 == 0:
        continue
    print(odd_numbers)
