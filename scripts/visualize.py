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

# # Plot 3
# # Mariah Carey's data
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
# mc_data = songs[songs['artist_name'] == "Mariah Carey"]['year']
# labels = list(range(mc_data.values.min(),mc_data.values.max()+1))

# # ax[0] = fig.add_subplot(1,2,1)
# sns.countplot(mc_data, order=labels, ax=ax[0])
# ax[0].tick_params(axis='x', labelrotation=45)
# ax[0].set_title("Mariah Carey's #1s By Year")

# # The Beatles' data
# sns.countplot(songs[songs['artist_name'] == "The Beatles"]['year'], ax=ax[1])
# ax[1].set_title("The Beatles' #1s By Year")
# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/mariah-vs-beatles.png",
# 			bbox_inches='tight')

# # Plot 4
# get top 12 artists with the most number 1 hits
top_12_artists = list(songs['artist_name'].value_counts()[:12].index)

# fig = plt.figure(figsize=(30,20))
# fig.subplots_adjust(hspace=0.4, wspace=0.2)
# for i in range(1, 13):
#     ax = fig.add_subplot(4, 3, i)
#     artist = top_12_artists[i-1]

#     data = songs[songs['artist_name'] == artist]['year']
#     labels = list(range(data.values.min(),data.values.max()+1))
#     ax.set_title(f"Total #1 Hits by Year: {artist}")
#     ax.set_xticklabels(labels, rotation=45)
#     sns.countplot(data, order=labels )

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/top-artist-hits-by-year.png",
# 			bbox_inches='tight')

# Plot 5
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
colors.extend(colors)
cols = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 
        'liveness', 'valence', 'tempo', 'zero_crossing_rate', 'duration_ms']

# fig = plt.figure(figsize=(15,15))
# fig.subplots_adjust(hspace=0.4, wspace=0.2)
# fig.suptitle("Audio Feature Distributions for Number One Singles from 1950s to Present", 
#              y=0.92, fontsize=20)

# for i in range(1, 13):
#     ax = fig.add_subplot(4, 3, i)
#     feature = cols[i-1]

#     ax.set_title(cols[i-1])
#     sns.distplot(songs[cols[i-1]], color=colors[i-1], hist_kws=dict(alpha=0.8))

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/audio-feature-distributions.png",
# 			bbox_inches='tight')

# Plot 6
# fig, ax = plt.subplots(figsize=(15,10))
# plt.title("Correlation Between Audio Features (Pearson's R)", fontsize=20)
# corr = songs[cols].corr()
# sns.heatmap(corr, annot=True, fmt='.1g',vmin=0, vmax=1)

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/audio-feature-heatmap.png",
# 			bbox_inches='tight')

# Plot 7
decade_grouped = songs.groupby(['decade']).mean().reset_index()

fig = plt.figure(figsize=(20,20))
fig.subplots_adjust(hspace=0.3, wspace=0.2)
for i in range(1, 13):
    ax = fig.add_subplot(4, 3, i)
    feature = cols[i-1]

    sns.barplot(x='decade', y=cols[i-1], data=decade_grouped)
    ax.set_title(cols[i-1])

plt.show()