def make_album(artist_name, album_title, num_tracks = ''):
    '''function that builds a dictionary of a music album'''
#the if-else statement checks to see if the argument num_tracks has any input
#-if it does, include the parameter in the dictionary, if not, then skip 
    if num_tracks:
        album = {'artist' : artist_name, 'album' : album_title,
    'number of tracks' : num_tracks, }
    else:
        album = {'artist' : artist_name, 'album' : album_title }
    return album
    
while True:
    print('\nCreate a file on your favorite albums!')
    print("Enter 'stop' to quit.")
    artist_name = input('Enter a band name: ')
    if artist_name == 'stop':
        break
        
    album_title = input('Enter the name of the album: ')
    if album_title == 'stop':
        break
    num_tracks = str(input('Enter the number of tracks on the album: '))
    if num_tracks == 'stop':
        break
    
#the value of artist_name is stored with the key 'artist'
#the value of album_title is stored with the key 'album'

music = make_album()
print(music)
