import owlready2 as owl
import music21 as music
import os
import json


def get_midi_file_names():
    files = []
    for file in os.listdir("./midi-files"):
        files.append(file)

    return files


def main():
    files = get_midi_file_names()
    print(files)


if __name__ == "__main__":
    main()
