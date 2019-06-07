"""
This module will query the OWL Ontology based on a user's inputted genre to 
    select a set of instruments as midi program integers
"""
import owlready2 as owl


def load_ontology():
    return owl.get_ontology("root-ontology.owl").load()


def get_genre_map(ontology):
    genres = {}

    key = 0
    for individual in ontology.search(type=ontology.MusicalGenre):
        genres.update({key: individual})
        key += 1

    return genres


def get_instruments(genre, ontology):
    programs = []
    if genre.label[0] == "Blues":
        programs.append(26)
        programs.append(23)
        programs.append(118)
    elif genre.label[0] == "Folk":
        programs.append(106)
        programs.append(33)
        programs.append(4)
    elif genre.label[0] == "Rock":
        programs.append(28)
        programs.append(34)
        programs.append(119)
    elif genre.label[0] == "Classical":
        programs.append(41)
        programs.append(69)
        programs.append(74)
        programs.append(43)
    elif genre.label[0] == "Country":
        programs.append(26)
        programs.append(111)
        programs.append(118)
    return programs
