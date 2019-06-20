cash_money = ['clams', 'bones', 'duckets', 'snortskis']
print(cash_money[-4].upper())
print(cash_money)
#we are replacing the first item in the list 'clams' with 'nose clams'
cash_money[0] = 'nose clams'
print(cash_money[0])
print(cash_money)

#we can also add to the end of a list with the .append command
cash_money.append('jacksons')
print(cash_money)

streets = [] 
streets.append ('Autobahn')
streets.append ('Beverly')
print(streets)
print(streets[0].upper())

streets.insert(1, 'Calumet')
print(streets)

del streets[2]
print(streets)
streets.append ('Darwin')
streets.insert(0, 'Faraday')
streets.append ('beverly')
print(streets)
#notice insert is variable.insert( position, 'string')
#while delete is del variable[position]

loser_streets = streets.pop(1)
print(streets)
print(loser_streets)
#.pop takes the last item in a list and removes it
#we created a new variable (loser_streets) and made it = to the removed
#items from .pop

message = 'The last street I lived on was ' + loser_streets.upper() + ", thank god I don't anymore!"
print(message)

brotherman = 'beverly'
streets.remove(brotherman)
print(streets)
print('I currently live on ' + brotherman + ', for how long we will see')

