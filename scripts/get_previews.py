import pandas as pd 
import numpy as np 
import requests
from IPython.display import clear_output

def get_mp3(track_id, url):
	'''A function that takes an mp3 url, and writes it to the local
		directory "/tmp"'''
	doc = requests.get(url)
	with open(f'C:/Users/deand/Documents/Repositories/Music-Analysis/data/previews/track_{track_id}.wav', 'wb') as f:
		f.write(doc.content)



songs = pd.read_csv("C:/Users/deand/Documents/Repositories/Music-Analysis/data/all_decades_songs_V3.csv", index_col=0)

err = {}
for i, row in songs.iterrows():
	try:
		get_mp3(row['track_id'], row['preview_url'])

	except:
		err[row['track_id']] = row['preview_url']

	clear_output(wait=True)
	print(f"{i+1}/{len(songs)}")

print(err)

