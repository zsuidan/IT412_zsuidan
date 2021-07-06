from functions.playlist_functions import *

playlist = []

add_more = True

while add_more:
    new_song = input("Enter a song name: ")
    new_artist = input("Enter the artist name (leave blank if unknown): ")

    if new_artist:
        playlist.append(add_song(new_song, new_artist))
    else:
        playlist.append(add_song(new_song))

    continue_adding = input("Would you like to add another song? (Y/N): ")

    correct_input = False

    while not correct_input:
        if continue_adding.upper() == "Y" or continue_adding.upper() == "N":
            correct_input = True
        else:
            continue_adding = input("Invalid response. Please enter either Y or N.")
    
    if continue_adding.upper() == "N":
        break

show_playlist(playlist)