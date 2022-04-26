import csv

def menu(login,register):
    menu = input("Welcome to OCR's greatest music app. To register press 'r'. To login press 'l':")
    if menu == "r":
        register()
    elif menu == "l":
        login()
    
    
        
def register():
    username = input("Please create a username:")
    password = input("Please create a password:")
    name = input("Please enter your name:")
    dob = input("Please enter your Date of Birth:")
    fave_artist = input("Please enter your favourite artist:")
    fave_genre = input("Please enter your favourite genre:")
    writefile = open("Account.csv","a")
    writefile.write(username + ',' + password + ',' + name + ',' + dob + ',' + fave_artist + ',' + fave_genre + '\n')
    writefile.close()
    menu(login,register)  
    
def login():
    checkusername = input("Please enter existing username:")
    checkpassword = input("Please enter existing password:")
    file=open("Account.csv","r")
    found=False 
    for line in file:
        Account=line.split(",") 
    if checkusername == Account[0]:
        if checkpassword == Account[1]:
            with open('Account.csv', 'r') as file:
                 reader = csv.reader(file)
                 print("Welcome!")
                 song_library(playlists,add_songs,view_songs)
    else:
        print("Access Denied! Check Username and Password!")
    menu(login,register)
        
def song_library(playlists,add_songs,view_songs):
    song_library = input("To add new songs press '1'. To view your song library press '2'. To go to your playlists press '3' Or to log out press 4:")
    if song_library == "1":
        add_songs()
    elif song_library == "2":
        view_songs()
    elif song_library == "3":
        playlists(create,view)
    elif song_library == "4":
        menu(login,register)
    
        
def add_songs():
        song_title = input("Please enter your new song title:")
        artist_name = input("Please enter the artist's name:")
        writefile = open("Song library.txt", "a")
        writefile.write('\n' + song_title + ' ' + '-' + ' ' + artist_name  + '\n')
        writefile.close()
        song_library(playlists,add_songs,view_songs)

def view_songs():
    with open('Song library.txt', 'r') as r:
         for line in sorted(r):
            print( line , end='')
         song_library(playlists,add_songs,view_songs)
         
    
    
               
def playlists(create,view):
    playlist = input("To create a playlist press 1 else press 2 to view other playlsits or press 3 to return to main menu:")
    if playlist == "1":
        create()
    elif playlist == "2":
        view()
    elif playlist == "3":
        song_library(playlists,add_songs,view_songs)
    

def create():
    time_limit = (input("Please enter the time limit you would like the plsylist to last till:"))
    genre = input("Please enter the genre you would like your playlist to be:")
    artists_name = input("Please enter an artists name:")
    writefile = open("Playlists.txt", "a")
    writefile.write(time_limit + ',' + genre + ',' + artists_name + '\n')
    writefile.close()
    song_library(playlists,add_songs,view_songs)
    
    

def view():
     with open('Playlists.txt', 'r') as r:
         for line in sorted(r):
             print(line , end='')
    
    
            


menu(login,register)
song_library(playlists,add_songs,view_songs)
playlists(create,view)
add_songs()
view_songs()
login()


