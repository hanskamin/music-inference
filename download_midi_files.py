# This script scrapes the links to MIDI files and downloads each of the
# actual files into our repository.

from bs4 import BeautifulSoup
import pandas as pd
import requests

def download_midi_file(link):
    # The filename is all the text after the final slash.
    filename = 'midi-files/%s' % link.rsplit('/', 1)[-1]
    with open(filename, 'wb') as file:
        download = requests.get(link)
        file.write(download.content)

song_info = pd.read_csv('songs.csv')
song_info['link'].apply(download_midi_file)
