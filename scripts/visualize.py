import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

songs = pd.read_csv("C:/Users/deand/Documents/Repositories/Music-Analysis/data/processed/final_dataset_year.csv", index_col=0)

# Plots to generate:
# 1. Histogram: number of songs per decade
# 2. Histogram: number of songs per year
# 3. Histogram subplots: Mariah Carey vs. The Beatles
# 4. Histogram subplots: All top hitmakers - songs per year
# 5. KDE: distribution of features
# 6. Heatmap of features
# 7. Histogram subplot of mean features by decade
# 8. Line plot: mean features by year
# 9. Diagnostic plots: show data is not normal
# 10. Heatmaps: result of Dunn's test for danceability, energy, valence
# 11. Line plots: accompany heatmaps

# # Plot 1
# sns.countplot(x = 'decade', data=songs)
# plt.xlabel('Decade')
# plt.ylabel('Count')
# plt.title("Total #1 Hits By Decade")
# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/number-one-counts-decade.png",
# 			bbox_inches='tight')

# # Plot 2
# fig, ax = plt.subplots(figsize=(50,15))
# sns.countplot(x='year', data=songs)

# e = 2
# for n,label in enumerate(ax.xaxis.get_ticklabels()):
#     if n%e !=0:
#         label.set_visible(False)

# plt.xlabel('Year', fontsize=40)
# plt.ylabel('Count', fontsize=40)
# plt.xticks(rotation=45, fontsize=30)
# plt.yticks(fontsize=30)
# plt.title("Total #1 Hits By Year", fontsize=50)
# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/number-one-counts-year.png",
# 			bbox_inches='tight')

# Plot 3
# Mariah Carey's data
fig, ax = plt.subplots(figsize=(10,5))
data = songs[songs['artist_name'] == "Mariah Carey"]['year']
labels = list(range(data.values.min(),data.values.max()+1))

sns.countplot(data, order=labels)
plt.xticks(rotation=45)
plt.title("Mariah Carey's #1s By Year")
plt.show()

# The Beatles' data
fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(songs[songs['artist_name'] == "The Beatles"]['year'])

plt.title("The Beatles' #1s By Year")
plt.show()