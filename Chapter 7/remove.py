cars = ['bmw', 'audi', 'ford', 'fiat', 'ford', 'bens', 'chevy', 
    'ford', 'chrysler']
print(cars)

while 'ford' in cars:
#while the value of 'ford' is in the list, keep running it. 
    cars.remove('ford')
print(cars)
