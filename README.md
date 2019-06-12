# music-inference

Using an OWL Ontology and neural network to classify songs and recreate them in different genres.

# Setup:

## Install Necessary Dependencies

### owlready2: OWL python API

-  documentation and project site: https://pypi.org/project/Owlready2/
-  `pip3 install Owlready2`

### music21: MIDI and musicology libraries

-  documentation and project site: http://web.mit.edu/music21/doc/index.html
-  `pip3 install music21`
-  dependency: matplotlib
-  `pip3 install matplotlib`

### BeautifulSoup: web scraping

-  documentation and project site: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
-  `pip3 install beautifulsoup4`

### pandas: data analysis & manipulation

-  documentation and project site: http://pandas.pydata.org/pandas-docs/stable/
-  `pip3 install pandas`

### requests: http library

-  documentation and project site: https://2.python-requests.org/en/master/
-  `pip3 install requests`

### tensorflow: machine learning library

-  documentation and project site: https://www.tensorflow.org/
-  `pip3 install tensorflow`

### keras: wrapper API for tensorflow

-  documentation and project site: https://keras.io/
-  `pip3 install keras`

## Import libraries as needed in a python script

-  `import owlready2 as owl`
-  `import music21 as music`
-  `from bs4 import BeautifulSoup`
-  `import pandas as pd`
-  `import requests`
-  `from keras import Sequential`

## TODO:

-  Figure out inputs, layers, outputs, etc.
-  Train our network.

## Resources and Examples:
-  [MIDI instruments and their associated roles](https://soundprogramming.net/file-formats/general-midi-instrument-list/)
