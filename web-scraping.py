import requests
from bs4 import BeautifulSoup
import pandas as pd

webpage_response = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2000s')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

date = []
artist = []
song = []

pizza = soup.find_all('td')

x = 5
for i in range(129):
    if (pizza[x].string):
        date.append((pizza[x].string))
    else:
        date.append((pizza[x].a.string))
    if (pizza[x+1].string):
        artist.append((pizza[x+1].string))
    else:
        artist.append((pizza[x+1].a.string))
    if (pizza[x+2].string):
        song.append((pizza[x+2].string))
    else:
        song.append((pizza[x+2].a.string))
    x += 7

data = {'Date': date, 'Artist': artist, 'Song': song}

number_ones = pd.DataFrame(data)

number_ones.to_csv('top_2000s.csv')