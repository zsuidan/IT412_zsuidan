def add_song(passed_song_name, passed_artist='Unknown'):
    """Creates a dictionary for a song and artist using user input
    Arguments: 
        passed_song_name -- song name entered by user
        passed_artist -- artist name entered by user
    Returns:
        dictionary entry with a song name and artist
    """

    returned_dictionary = {'song_name': str(passed_song_name), 'artist': str(passed_artist)}

    return returned_dictionary

def show_playlist(passed_playlist):
    """Loops through a list of songs in a playlist printing each one out with its name and artist
    Arguments: 
        passed_playlist [list of dictionaries] -- each dictionary has the format of {'song_name': str(passed_song_name), 'artist': str(passed_artist)}
    Returns:
        a series of printed lines detailing the song names and artists in the playlist, one line for each dictionary entry in the passed_playlist
    """

    for song in passed_playlist:
        print("Song: " + song['song_name'] + "\t\tArtist: " + song['artist'])