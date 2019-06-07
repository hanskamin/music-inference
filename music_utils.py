"""
This module contains utility functions that deal with MIDI files and their 
    music21 object representations
"""
from music21 import converter, instrument, note, chord, stream
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

    return sorted(files)


def get_some_files(stepSize):
    all_files = get_midi_file_names()
    ret_files = []

    ct = 0
    for file in all_files:
        if ct % stepSize:
            ct += 1
            continue
        else:
            ct += 1
            ret_files.append(file)

    return ret_files


def get_notes():
    notes = []
    prefix = "./midi-files/"
    files = get_some_files(20)
    remaining = len(files)
    done = 0
    for file in files:
        # pretty_print_progress(done, remaining)
        print("Parsing:", file)

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


def create_midi(prediction_output, genre_name, midi_programs):
    # NOTE: use instrument.instrumentFromMidiProgram(int) to provide a track with its instrument
    # convert network's prediction into music21-readable format, and then into a MIDI file
    print("Generating MIDI File...")

    midi_stream = stream.Score()
    for program in midi_programs:
        offset = 0
        output_notes = []
        for pattern in prediction_output:
            if "." in pattern or pattern.isdigit():
                notes_in_chord = pattern.split(".")
                notes = []
                for current in notes_in_chord:
                    new_note = note.Note(int(current))
                    notes.append(new_note)
                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                output_notes.append(new_chord)
            else:
                new_note = note.Note(pattern)
                new_note.offset = offset
                output_notes.append(new_note)

            offset += 0.5

        midi_part = stream.Part(output_notes)
        # set the part's instrument
        midi_part.insert(0, instrument.instrumentFromMidiProgram(program))
        # insert instrument part into score object
        midi_stream.insert(0, midi_part)

    # write score to file
    midi_stream.write("midi", fp="test_output.mid")
