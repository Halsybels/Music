def menu(login,register):
    menu = input("Welcome to OCR's greatest music app. Choose either to register by pressing 1 else type anything else:")
    if menu == "1":
        register()
    else:
        login()

        
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
    
def login():
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
    song_list = input("Would you like to see your song titles?")
    if song_list == 'yes':
        with open('Songs.txt', 'r') as r:
         for line in sorted(r):
            print( line , end='')
    
                
def playlists(create,view):
    
    playlists = input("Would you like to create a playlist if so press 1 else press 2 to view other playlsits:")
    if playlists == "1":
        create()
    else:
        view()
    

def create():
    time_limit = (input("Please enter the time limit you would like the plsylist to last till:"))
    genre = input("Please enter the genre you would like your playlist to be:")
    artists_name = input("Please enter an artists name:")
    writefile = open("Playlists.txt" , "a")
    writefile.write('\n' + time_limit + ',' + genre + ',' + artists_name + '.')
    writefile.close()


def view():
     with open('Playlists.txt', 'r') as r:
         for line in sorted(r):
            print( line , end='')


menu(login,register)  
playlists(create,view)


