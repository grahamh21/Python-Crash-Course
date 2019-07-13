users = {'kristin524' : {'first':'kristin', 'last':'burke', 'city':'buffalo'},
    'kendra99': {'first': 'kendra', 'last': 'burke', 'city' : 'rochester'},
    'katie23' : {'first': 'katie', 'last' : 'corbett', 'city' : 'webster', } 
    }
for username, info in users.items():
    print('Username:\t' + username)
    full_name = info['first'] + ' ' + info['last']
    location = info['city']
    print('Full name: \t' + full_name)
    print('Location: \t' + location)
    print('\t')
#nested dictionaries - created variables by combining values of specific 
#first dictionary values
