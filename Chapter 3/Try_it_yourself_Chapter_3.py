#Try It yourself 3-1

tiy = 'Try It Yourself 3-1'
print(tiy)
gay_friends = ['Tom', 'Clancy', "Geroge", 'LARRY', 'Veronica']
print(gay_friends[-2].title())
print(gay_friends[0].upper() + '\n')


tiy = 'Try It Yourself 3-2'
#Try It yourself 3-2
print(tiy)
friend_message = 'Hello my gay friend '
friend_message2 = ', how are you feeling?'
print(friend_message + gay_friends[0].title() + friend_message2)
print(friend_message + gay_friends[1].title() + friend_message2)
print(friend_message + gay_friends[2].title() + friend_message2)
print(friend_message + gay_friends[3].title() + friend_message2)

#Try It yourself 3-4
print('\nTry It Yourself 3-4')

dinner_guests = ['bill burr', 'nomar g', 'boy george']
print('Hello ' + dinner_guests[0].title() + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[1].upper() + ', nice to see you for dinner!')

#Try It yourself 3-5
print('\nTry It Yourself 3-5')
print('Rats! Our dinner guest ' + dinner_guests[2].title() + ' cannot make it tonight!')
nodinner = dinner_guests.pop()
dinner_guests.append ('little richard')
print('sorry ' + nodinner.upper() + ', you can come next time!')
print('We are still having dinner ' + dinner_guests[0].title() + ', welcome home!')
print('We are still having dinner ' + dinner_guests[1].title() + ', welcome home!')
print('We are still having dinner ' + dinner_guests[2].title() + ', welcome home!')


#Try It yourself 3-6
print('\nTry It Yourself 3-6')
dinner_guests.insert(0, 'Lee')
dinner_guests.insert(2, 'Carla')
dinner_guests.append('Claire')
print(dinner_guests)
print('Hello ' + dinner_guests[0] + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[1] + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[2] + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[3] + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[4] + ', nice to see you for dinner!')
print('Hello ' + dinner_guests[5] + ', nice to see you for dinner!')

#Try It yourself 3-7
print('\nTry It Yourself 3-7')
print('Table was slow =(')
#
print(dinner_guests)
loser_guests = dinner_guests.pop()
print(dinner_guests)
print('Sorry ' + loser_guests + ', table too small!')
loser_guests = dinner_guests.pop(0)
print('Sorry ' + loser_guests + ', table too small!')
loser_guests = dinner_guests.pop(0)
print('Sorry ' + loser_guests + ', table too small!')
loser_guests = dinner_guests.pop(0)
print('Sorry ' + loser_guests + ', table too small!')
print(dinner_guests)
print('Good job winner!' + dinner_guests[0])
print('Good job winner!' + dinner_guests[1])
print(dinner_guests)
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)


#Try It yourself 3-9
print('\nTry It Yourself 3-9')
print('There are ' + str(len(loser_guests)) + ' loser guests!')
