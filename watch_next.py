# The code takes in the description as a parameter and reads movies.txt. Then it returns the title of the most similar movie.


# importing spacy 
import spacy
nlp = spacy.load('en_core_web_md')


# watch_next function to determines which movies a user would watch next according to given description.
# movies.txt is read and the file is shredded and thrown into the lists (films and names).
# The similarity of the films is calculated and the rates are added to similarity_list.
# The index of the maximum rate is equal to the index of the movie to be rotated in the name list.

def watch_next(description):

    films = []
    names = []
    similarity_list = []

    file = open("movies.txt", "r")

    for i in file:
        i = i[:-1]
        films.append(i.split(" :")[1])
        names.append(i.split(" :")[0])


    model_film = nlp(description)

    for film in films:
        similarity = nlp(film).similarity(model_film)
        similarity_list.append(similarity)

    return f"Your next movie: {names[similarity_list.index(max(similarity_list))]}"


description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

watch_next(description)
