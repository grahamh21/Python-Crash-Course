def emails(unconfirmedEmail, confirmedEmail, ):
    while unconfirmedEmail:
        currentEmail = unconfirmedEmail.pop()
        print('confirming email: ' + currentEmail)
        confirmedEmail.append(currentEmail)

def show_confirmed_emails(confirmedEmail):
    '''show all the emails that were confirmed'''
    print('\nThe following email has been confirmed: ')
    for confirmed_email in confirmedEmail:
        print(confirmed_email)

unconfirmedEmail = ['graham@aol.com', 'leo@aol.com', 'mark@aol.com']
confirmedEmail = []

#make sure the parameters are in the correct order, I had them backwards
#and nothing showed up
emails( unconfirmedEmail, confirmedEmail)
show_confirmed_emails(confirmedEmail)
