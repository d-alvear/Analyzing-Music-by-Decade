import requests
from bs4 import BeautifulSoup
import pandas as pd

webpage_response = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2010s')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

tables = soup.find_all('table')
dates = []
artists = []
songs = []

for tr in tables[2].find_all('tr'):
    tds = tr.find_all('td')
    if not tds:
        continue
    date, artist, song = [td.text.strip() for td in tds[1:4]]
    dates.append(date)
    artists.append(artist)
    songs.append(song.replace('♪',''))

data = {'Date': dates, 'Artist': artists, 'Song': songs}

number_ones = pd.DataFrame(data)

number_ones.to_csv('top_2010.csv')

