# music-inference
Using an OWL Ontology and neural network to classify songs and recreate them in different genres.

# Setup:
## Install Necessary Dependencies
### owlready2: OWL python API
 - documentation and project site: https://pypi.org/project/Owlready2/
 - `pip3 install Owlready2`
### music21: MIDI and musicology libraries
- documentation and project site: http://web.mit.edu/music21/doc/index.html
- `pip3 install music21`
### BeautifulSoup: web scraping
- documentation and project site: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- `pip3 install beautifulsoup4`
### pandas: data analysis & manipulation
- documentation and project site: http://pandas.pydata.org/pandas-docs/stable/
- `pip3 install pandas`
### requests: http library
- documentation and project site: https://2.python-requests.org/en/master/
- `pip3 install requests`

## Import libraries as needed in a python script
 - `import owlready2 as owl`
 - `import music21 as music`
 - `from bs4 import BeautifulSoup`
 - `import pandas as pd`
 - `import requests`
 

## TODO:
- Make JSON file for filling ontology.
- Figure out inputs, layers, outputs, etc.
- Train our network.

## Resources and Examples:
- [Generating Music with a Recurrent NN](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5)
- [MIDI instruments and their associated roles](https://soundprogramming.net/file-formats/general-midi-instrument-list/)
