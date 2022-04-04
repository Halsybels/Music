def menu(login,register):
    menu = input("Welcome to OCR's greatest music app. To register press 'r'. To login press 'l':")
    if menu == "r":
        register()
    elif menu == "l":
        login(playlists,add_songs,view_songs)
    
    
        
def register():
    username = input("Please create a username:")
    password = input("Please create a password:")
    name = input("Please enter your name:")
    dob = input("Please enter your Date of Birth:")
    fave_artist = input("Please enter your favourite artist:")
    fave_genre = input("Please enter your favourite genre:")
    writefile = open("Account.txt","w")
    writefile.write(username + '\n' + password + '\n' + name + '\n' + dob + '\n' + fave_artist + '\n' + fave_genre + '\n')
    writefile.close()
    menu(login,register)  
    
def login(playlists,add_songs,view_songs):
    checkusername = input("Please enter existing username:")
    checkpassword = input("Please enter existing password:")
    file = open('Account.txt' , 'r')
    u = file.readline().strip()
    p = file.readline().strip()
    if checkusername + checkpassword == u + p :
        print("Welcome!")   
    else:
        print("Access denied! Check Username and Password.")
        file.close()
    view_songs = input("Would you like to view your songs?")
    create_playlist = input("Would you like to create a playlist?")
    add_songs = input("Would you like to add a new song to your song library?")
    if add_songs == "yes" or "Yes":
        add_songs()
    else:
        menu(login,register)

    if view_songs == "yes" or "Yes":
        view_songs()
    else:
        menu(login,register)
    if create_playlists == "yes" or "Yes":
        playlists(create,view)
    else:
        menu(login,register)
    
        
def add_songs():
        song_title = input("Please enter your new song title:")
        artist_name = input("Please enter the artist's name:")
        song_length = input("Please enter the song length:")
        writefile = open("Song library.txt", "a")
        writefile.write(song_title + '-' + artist_name + '-' + song_length + '\n')
        writefile.close()

def view_songs():
    with open('Song library.txt', 'r') as r:
         for line in sorted(r):
            print( line , end='')
    
               
def playlists(create,view):
    playlists = input("To create a playlist press 1 else press 2 to view other playlsits or press 3 to return to main menu:")
    if playlists == "1":
        create()
    elif playlists == "2":
        view()
    elif playlists == "3":
        menu(login,register)
    

def create():
    time_limit = (input("Please enter the time limit you would like the plsylist to last till:"))
    genre = input("Please enter the genre you would like your playlist to be:")
    artists_name = input("Please enter an artists name:")
    writefile = open("Playlists.txt" , "x")
    writefile.write('\n' + time_limit + ',' + genre + ',' + artists_name + '.')
    writefile.close()


def view():
     with open('Playlists.txt', 'r') as r:
         for line in sorted(r):
            print( line , end='')


menu(login,register)
playlists(create,view)



