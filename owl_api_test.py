import owlready2 as owl
import json


# IRI's for individuals, classes, and props added online vs in the client have different
#   conventions, and the client ones often lack a label by default. Add labels to everything
#   so that we can always access a member by its label
def add_onto_labels(ontology):
    print("Adding labels to ontology")
    members = [ontology.classes(), ontology.properties(),
               ontology.individuals()]

    for member in members:
        for entry in member:
            if entry.label == []:
                entry.label = [entry.name]

    ontology.save("root-ontology.owl")


def get_MIDI_instruments():
    with open("instrument_list.json", "r") as fp:
        instList = json.load(fp)

    instruments = []
    for idx in instList:
        instruments.append((idx, instList[idx]))

    return instruments


def print_onto(ontology):
    print("\n~~~~~~~~Printing Ontology~~~~~~~~")

    # classes
    print("\nClasses:")
    for ontoClass in ontology.classes():
        print(ontoClass.label[0])

    # object properties
    print("\nObject Properties:")
    for prop in ontology.object_properties():
        try:
            propRange = prop.range[0].label[0]
            propDomain = prop.domain[0].label[0]
            print(prop.label[0], ": (", propDomain,
                  "->", propRange, ")")
        except IndexError:
            print(
                prop.label[0], ": either range or domain is not currently specified")

    # individuals
    print("\nIndividuals:")
    for ontoClass in ontology.classes():
        print("... of class", ontoClass.label[0])
        try:
            for individual in ontology.search(type=ontoClass):
                print("\t", individual.label[0])
        except:
            continue


def create_instrument_individual(ontology, instrumentName, midiKey):
    newInstrument = ontology.Instrument(instrumentName)
    newInstrument.label = [instrumentName]
    newInstrument.midiKey = [int(midiKey)]


def remove_instruments(ontology):
    print("removing instruments")
    instruments = ontology.search(type=ontology.Instrument)
    for instrument in instruments:
        owl.destroy_entity(instrument)


def print_instrument_relations(ontology):
    print("printing genres:")
    for genre in ontology.search(type=ontology.MusicalGenre):
        print("Genre:", genre.label[0])
        print("\tInstruments:")
        for instrument in genre.commonlyUsesInstrument:
            print("\t", instrument.label[0])


def main():
    ontology = owl.get_ontology("./root-ontology.owl").load()
    print()
    for instrument in get_MIDI_instruments():
        create_instrument_individual(ontology, instrument[1], instrument[0])
    print_onto(ontology)
    ontology.save("./root-ontology.owl")


if __name__ == "__main__":
    main()
