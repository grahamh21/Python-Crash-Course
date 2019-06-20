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
