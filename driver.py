"""
This module serves as the main entry point for the program. It will house the CLI, asking the 
   user for a genre, and passing the resultant instrument selections to the machine learning
   module to generate instrument tracks which will be packaged into a MIDI output file
"""
import music_generator as generator
import onto_utils


def get_genre_selection():
    print("""Select one of the Following Genres:
    [0] Blues
    [1] Folk
    [2] Rock
    [3] Classical
    [4] Country""")

    key = -1
    while key < 0:
        try:
            selection = int(input("Selection: "))
            key = get_genre_key(selection)
        except:
            print("Please Enter a Valid Option.")
            continue

        if key < 0:
            print("Please Enter a Valid Option.")
            continue

    return key


def get_genre_key(selection):
    if selection == 0:
        return 3
    elif selection == 1:
        return 11
    elif selection == 2:
        return 17
    elif selection == 3:
        return 5
    elif selection == 4:
        return 8
    else:
        return -1


def main():
    ontology = onto_utils.load_ontology()
    genres = onto_utils.get_genre_map(ontology)

    selection = get_genre_selection()
    print("Selected:", genres[selection].label[0])
    print("Instruments in Genre:")
    midiPrograms = onto_utils.get_instruments(genres[selection], ontology)

    generator.generate_song(genres[selection], midiPrograms)


if __name__ == "__main__":
    main()

# generator.generate_track()
