"""
This module contains functions that set up the LSTM RNN and package input data for training and subsequent 
   serialization of the trained network
"""
from keras.models import Sequential
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
