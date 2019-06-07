"""
This module will query the OWL Ontology based on a user's inputted genre to 
    select a set of instruments as midi program integers
"""
import owlready2 as owl
from music21 import instrument


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
        programs.append(instrument.AcousticGuitar().midiProgram)
        programs.append(instrument.Harmonica().midiProgram)
        programs.append(instrument.TomTom().midiProgram)
    elif genre.label[0] == "Folk":
        programs.append(instrument.Banjo().midiProgram)
        programs.append(instrument.AcousticBass().midiProgram)
        programs.append(instrument.Piano().midiProgram)
    elif genre.label[0] == "Rock":
        programs.append(instrument.ElectricGuitar().midiProgram)
        programs.append(instrument.ElectricBass().midiProgram)
        programs.append(instrument.BassDrum().midiProgram)
    elif genre.label[0] == "Classical":
        programs.append(instrument.Violin().midiProgram)
        programs.append(instrument.Oboe().midiProgram)
        programs.append(instrument.Flute().midiProgram)
        programs.append(instrument.Viola().midiProgram)
    elif genre.label[0] == "Country":
        programs.append(instrument.AcousticGuitar().midiProgram)
        programs.append(instrument.Banjo().midiProgram)
        programs.append(instrument.TomTom().midiProgram)
    return programs
