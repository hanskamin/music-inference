import owlready2 as owl


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


def print_onto(ontology):
    print("\n~~~~~~~~Printing Ontology~~~~~~~~")

    # classes
    print("\nClasses:")
    for ontoClass in ontology.classes():
        print(ontoClass.label[0])

    # object properties
    print("\nObject Properties:")
    for prop in ontology.object_properties():
        propRange = prop.range
        propDomain = prop.domain
        print(prop.label[0], ": (", propDomain, "->", propRange, ")")

    # individuals
    print("\nIndividuals:")
    for ontoClass in ontology.classes():
        print("... of class", ontoClass.label[0])
        for individual in ontology.search(type=ontoClass):
            print("\t", individual.label[0])


# parse ontology for further use
ontology = owl.get_ontology("./root-ontology.owl").load()

print()
add_onto_labels(ontology)
print_onto(ontology)
ontology.save("root-ontology.owl")
