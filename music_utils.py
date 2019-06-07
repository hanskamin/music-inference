"""
This module contains utility functions that deal with MIDI files and their 
    music21 object representations
"""
from music21 import converter, instrument, note, chord
import os
import pickle


def pretty_print_progress(done, remaining):
    total = done + remaining
    # value between 0 and 10
    progress = 100 * float(done) / float(total)

    print(" Done: %5d, Remaining: %5d | Progress: %5.2f%%" %
          (done, remaining, progress), end='\r')


def get_midi_file_names():
    files = []
    for file in os.listdir("./midi-files"):
        files.append(file)

    return files


def get_notes():
    notes = []
    prefix = "./midi-files/"
    files = get_midi_file_names()
    remaining = len(files)
    done = 0
    for file in get_midi_file_names():
        pretty_print_progress(done, remaining)
        midi = converter.parse(prefix + file)

        notes_to_parse = []
        try:  # multiple instrument parts
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        except:
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append(".".join(str(n) for n in element.normalOrder))

        done += 1
        remaining -= 1

    print()

    # this way we can recover the notes simply by deserializing later on
    with open("./song_data/notes", "wb") as file:
        pickle.dump(notes, file)

    return notes
