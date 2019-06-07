"""
This module contains functions that set up the LSTM RNN and package input data for training and subsequent
   serialization of the trained network
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
import numpy
import music_utils as utils


def init_training():
    # train a Neural Network to generate music
    notes = utils.get_notes()

    # get amount of pitch names
    n_vocab = len(set(notes))

    # pairings of input sequences with expected note/chord to be produced
    network_input, network_output = prepare_sequences(notes, n_vocab)

    model = create_network(network_input, n_vocab)

    train(model, network_input, network_output)


def prepare_sequences(notes, n_vocab):
    sequence_length = 100

    # omit duplicate notes from master list of notes, and sort notes
    pitch_names = sorted(set(item for item in notes))

    # create a dictionary mapping notes to integers
    note_to_int = dict((note, number)
                       for note, number in enumerate(pitch_names))

    network_input = []
    network_output = []

    # create input sequences and corresponding outputs
    for i in range(0, len(notes) - sequence_length, 1):
        # sequence of 100 notes or chords
        sequence_in = notes[i:i + sequence_length]
        # single note or chord
        sequence_out = notes[i + sequence_length]

        network_input.append([note_to_int[n] for n in sequence_in])
        network_output.append(note_to_int[sequence_out])

    n_patterns = len(network_input)

    # reshape network to be compatible with LSTM layers
    network_input = numpy.reshape(
        network_input, (n_patterns, sequence_length, 1))
    # normalize input
    network_input = network_input / float(n_vocab)

    network_output = np_utils.to_categorical(network_output)

    return (network_input, network_output)


def create_network(network_input, n_vocab):
    # create the structure of the neural network
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(network_input[1], network_input[2]), return_sequences=True
    ))
    model.add(Dropout(0.3))
    model.add(LSTM(512))
    model.add(Dense(256))
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    return model


def train(model, network_input, network_output):
    # train the neural network

    # format string with keyword format args
    filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor="loss",
        verbose=0,
        save_best_only=True,
        mode="min"
    )
    callbacks_list = [checkpoint]

    model.fit(network_input, network_output, epochs=200,
              batch_size=64, callbacks=callbacks_list)


if __name__ == "__main__":
    init_training()
