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

# Plot 1
plt.figure(figsize=(10,5))
ax = sns.countplot(x = 'decade', data=songs)
plt.xlabel('Decade')
plt.ylabel('Count')
plt.title("Total Number One Singles Per Decade")
for p in ax.patches:
    ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.27, p.get_height()+1))

plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/static/number-one-counts-decade.png",
			bbox_inches='tight')

# # Plot 2
# plt.figure(figsize=(50,15))
# ax = sns.countplot(x='year', data=songs)

# e = 2
# for n,label in enumerate(ax.xaxis.get_ticklabels()):
#     if n%e !=0:
#         label.set_visible(False)

# plt.xlabel('Year', fontsize=40)
# plt.ylabel('Count', fontsize=40)
# plt.xticks(rotation=45, fontsize=30)
# plt.yticks(fontsize=30)
# plt.title("Total Number One Singles Per Year", fontsize=50)
# for p in ax.patches:
#     ax.annotate('{}'.format(p.get_height()), (p.get_x(), p.get_height()+0.5), fontsize=30)

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/static/number-one-counts-year.png",
# 			bbox_inches='tight')

# Plot 3
# # Mariah Carey's data
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
# fig.subplots_adjust(hspace=0.2, wspace=0.1)
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
# sns.set_style(style='white')
# fig, ax = plt.subplots(figsize=(15,10))
# plt.title("Correlation Between Audio Features (Pearson's R)", fontsize=20)
# corr = songs[cols].corr()
# mask = np.zeros_like(corr)
# mask[np.triu_indices_from(mask)] = True

# sns.heatmap(corr, mask=mask, annot=True, fmt='.1g', vmin=0, vmax=1, square=True)

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/audio-feature-heatmap.png",
# 			bbox_inches='tight')

# sns.set_style(style='darkgrid')

# # Plot 7
# decade_grouped = songs.groupby(['decade']).mean().reset_index()

# fig = plt.figure(figsize=(15,15))
# fig.subplots_adjust(hspace=0.55, wspace=0.3)
# fig.suptitle("Mean Audio Features by Decade, 1950s to Present", 
#              y=0.92, fontsize=20)
# for i in range(1, 13):
#     ax = fig.add_subplot(4, 3, i)
#     feature = cols[i-1]

#     sns.barplot(x='decade', y=cols[i-1], data=decade_grouped)
#     ax.set_title(cols[i-1])

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/mean-audio-feature-decade.png",
# 			bbox_inches='tight')

# Plot 8, 9 - Don't need these

# Plot 10 & 11
# danceability = pd.read_csv("C:/Users/deand/Documents/Repositories/Music-Analysis/data/processed/stat-output/dunn_danceability.csv", index_col=0)
# energy = pd.read_csv("C:/Users/deand/Documents/Repositories/Music-Analysis/data/processed/stat-output/dunn_energy.csv", index_col=0)
# valence = pd.read_csv("C:/Users/deand/Documents/Repositories/Music-Analysis/data/processed/stat-output/dunn_valence.csv", index_col=0)

# sns.set_style(style='white')

# dfs = [danceability, energy, valence]
# titles = ['danceability', 'energy', 'valence']
# fig = plt.figure(figsize=(15,15))
# fig.subplots_adjust(hspace=0.2, wspace=0.2)

# for i,title,df in zip(range(1,4), titles, dfs):
#     ax = fig.add_subplot(2, 3, i)
#     mask = np.zeros_like(df, dtype=np.bool)
#     mask[np.triu_indices_from(mask)] = True
    
#     sns.heatmap(df, vmin=0, vmax=0.05, mask=mask, fmt='.1g', annot=True, cbar=False, square=True)
#     ax.set_title(f"{title.capitalize()}: Dunn's Test Results")

# sns.set_style(style='darkgrid')
# for i,title,c in zip(range(4,7), titles, colors):
#     ax = fig.add_subplot(2, 3, i)
#     plt.plot(songs.groupby('decade').mean()[title], marker="o", c=c)
#     ax.set_ylim((0.3,0.8))
#     ax.set_xlabel("Decade")
#     ax.set_ylabel(f"Mean {title.capitalize()}")
#     ax.set_title(f"Mean {title.capitalize()} by Decade")

# plt.savefig("C:/Users/deand/Documents/Repositories/Music-Analysis/reports/figures/static/test-result-plots.png",
# 			bbox_inches='tight')