#Try it yourself 8-6: City Names

def city_country(city, country):
    '''defines a city and country pair'''
    vacation = city + ', ' + country
    return vacation.title()
    
while True:   
    print('\nEnter a City and Country pair.')
    print("Press 'p' to stop")
    
    city_name = input('Name a city: ')
    if city_name == 'p':
        break
        
    country_name = input('What country is in the city in: ? ')
    if country_name =='p':
        break
    
    vacation_name = city_country(city_name, country_name)
    print(vacation_name)


    
print(city_country)

#Try it yourself 8-7: Album

def make_album(artist_name, album_title, num_tracks = ''):
    '''function that builds a dictionary of a music album'''
#the if-else statement checks to see if the argument num_tracks has any input
#-if it does, include the parameter in the dictionary, if not, then skip 
    if num_tracks:
        album = {'artist' : artist_name, 'album' : album_title,
    'number of tracks' : num_tracks, }
    else:
        album = {'artist' : artist_name, 'album' : album_title }
#the value of artist_name is stored with the key 'artist'
#the value of album_title is stored with the key 'album'
    return album
    
music = make_album('the black keys', 'el camino', 12)
print(music)
music = make_album('michael Jackson', 'thriller', 10)
print(music)
music = make_album('the black keys', 'brothers')
print(music)
#inputting names into the function return it in a dictionary 


#Try it yourself 8-8: User Albums
