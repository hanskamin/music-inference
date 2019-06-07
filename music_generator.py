"""
This module generates note sequences from a pre-trained network
"""
import pickle
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
import music_utils as utils


def generate_song(genre_name, midi_programs):
    # generate a midi track
    with open("./song_data/notes", "rb") as file:
        notes = pickle.load(file)

    # get all notes
    pitch_names = sorted(set(n for n in notes))
    n_vocab = len(pitch_names)

    network_input, normalized_input = prepare_sequences(
        notes, pitch_names, n_vocab)

    model = load_network(normalized_input, n_vocab)
    print("Predicting Note Sequences...")
    prediction_output = generate_notes(
        model, network_input, pitch_names, n_vocab)

    utils.create_midi(prediction_output, genre_name, midi_programs)


def prepare_sequences(notes, pitch_names, n_vocab):
    note_to_int = dict((note, number)
                       for number, note in enumerate(pitch_names))

    sequence_length = 100
    network_input = []
    output = []
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]

        network_input.append([note_to_int[n] for n in sequence_in])
        output.append(note_to_int[sequence_out])

    n_patterns = len(network_input)

    normalized_input = numpy.reshape(
        network_input, (n_patterns, sequence_length, 1))
    normalized_input = normalized_input / float(n_vocab)

    return (network_input, normalized_input)


def load_network(network_input, n_vocab):
    # recreate structure of NN used for training, this time with known weights
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(network_input.shape[1], network_input.shape[2]),
        return_sequences=True
    ))
    model.add(Dropout(0.3))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(512))
    model.add(Dense(256))
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    # Load the weights to each node
    model.load_weights("weights.hdf5")

    return model


def generate_notes(model, network_input, pitch_names, n_vocab):
    # pick a random note from NN based on sequence of notes:
    start = numpy.random.randint(0, len(network_input) - 1)

    int_to_note = dict((number, note)
                       for number, note in enumerate(pitch_names))

    pattern = network_input[start]
    prediction_output = []

    # generate 500 notes
    for note_idx in range(500):
        prediction_input = numpy.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(n_vocab)

        prediction = model.predict(prediction_input, verbose=0)

        # get index of most likely note
        index = numpy.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)

        pattern.append(result)
        # incorporate prediction into pattern for next feed-through
        pattern = pattern[1:len(pattern)]

    return prediction_output
