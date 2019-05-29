from bs4 import BeautifulSoup
from requests import get
import json

page_url = "https://www.midi.org/specifications/item/gm-level-1-sound-set"
page_response = get(page_url)
soup = BeautifulSoup(page_response.text, 'html.parser')
tables = soup.findAll("table")

instruments_map = {}
for row in tables[1].findAll("tr")[3:]:
    cells = row.findAll("td")

    number = int(cells[0].text.strip("."))
    instrument = cells[1].text

    instruments_map.update({number: instrument})

with open("./instrument_list.json", "w") as fp:
    json.dump(instruments_map, fp)
