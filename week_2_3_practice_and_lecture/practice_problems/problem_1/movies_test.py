#Opens a text file containing a list of favorite movies and adds a phrase to the end of each line while copying it to a new text file
with open("text_files/fav_movies_edited.txt", "w") as file_output:
    with open("text_files/fav_movies.txt") as txt_file:
        for line in txt_file:
            file_output.write(line.strip() + " is a movie I like\n")