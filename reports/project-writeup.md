# Analyzing Each Decade's Number-One Singles (1950s - 2010s)

![image](/reports/images/miriana-doroban-unsplash-copy.jpg)

<center><span>Photo by <a href="https://unsplash.com/@mirianaa_?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Miriana Dorobanțu</a> on <a href="https://unsplash.com/s/photos/records?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span></center>

## Introduction
<p></p>
There is no doubt that music has changed drastically over the past few decades. Great artists of the past are still highly regarded and have gone on to inspire other great artists in recent history. Several of my favorite musicians were pioneering music long before I was born, and have inspired some of my favorite modern musicians. This made me wonder about how music styles change over time, and if there are certain commonalites between hit songs from each decade.
<p></p>

### Goals
<p></p>
In this project, I perform an exploratory anlysis on singles that went number one on the Billboard Hot 100 Chart from the 1950s to present. I focused my analysis on answering the following questions:
<p></p>

* Which decade had the most number one singles?

* Which artists have the most number one singles?

* Are songs that go number one sung more by women or men? Solo acts or ensembles/groups?

* Of all songs that went number one since 1950, are there any commonalities between the songs? Like tempo, valence, etc. ?

* Is there any trends among audio features? (i.e. Does tempo stay consisent among the decades, or does it exhibit some type of cyclical pattern?)

* Are genres consistent among number ones? Do all songs have similar genres?

* Are songs in each decade distinct? Specifically, are songs in each decade statistically different than the others?

## Data
To find which singles went number one in each decade on the Billboard Hot 100 Chart, I went to the Wikipedia page for each decade's chart. From there, I wrote a script to scrape the information from the article and write it to a csv.

Then, I used the data collection pipeline I wrote for my app Friendshipify to request the song metadata and [audio features from the Spotify API](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/). I also used the feature extraction pipeline from Friendshipify to extract latent features from each song's preview. The final dataset contained the following features:

| Features | Description |
|---------|-------------|
|danceability| Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.|	
|energy	| Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.|
|key | The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.|
|loudness | The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.|	
|speechiness |Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. |
|acousticness |A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. |
|instrumentalness |Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. |
|liveness| Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.|	
|valence| A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).|	
|tempo | The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. |
|zero_crossing_rate |	The zero-crossing rate is the rate of sign-changes along a signal, i.e., the rate at which the signal changes from positive to zero to negative or from negative to zero to positive.|
|duration_ms| The duration of the song in milliseconds. |
|genres	| A list of genres assigned by Spotify.|
|year | The year the song was released. |
<p></p>

## Analysis

### 1. Which decade had the most number one singles?

<img src="figures\static\number-one-counts-decade.png">


I expected more recent decades to have the most number one singles due to the amount of music diversity there is today. However, it appears the 1970s had the most number one singles. The histogram above also shows an increasing trend in the amount of number one single from the 50s through the 70s. The amount of number one singles first starts in decrease in the 1980s, and continues this decreasing trend until today. 


I was curious about this decrease in singles and found an article from NME:

__NME: The number of unique Number One singles is decreasing.__

>In the ‘70s, the average number of Number Ones could be as high as 30 per year. In the past four years we haven’t had more than 13 unique Number Ones per year. As BBC Radio 1 boss Chris Price explained to NME last year, the stagnancy of the chart is probably down to streaming being counted in the charts: 
<br>
“We’ve moved away from somebody walking into HMV and being a physical single, or downloading a 99p download from iTunes, and we’re moving much more towards measuring engagement over time. It’s less like somebody walking into a shop and making a purchase, and more like somebody sitting at home in their bedroom and listening to something several times over.”
</blockquote>

[Source](https://www.nme.com/blogs/nme-blogs/billboard-100-shorter-explicit-2054269)  

The way we've started to listen to music has contributed to a drop in the amount of songs that go number one. After finding this out, I was interested in whether I coult pinpoint a specific year for this drop in number one hits, so I aggegated the counts by year to see the total songs that went number one in each year from 1950 to present.

<img src="figures\static\number-one-counts-year.png">

From the plot above, there are 3 major peaks in the amount of number ones per year. The peaks occur in the mid 60s and the mid 70s, with another persistent peak that started in the mid 80s and lasted through the early 90s. There are some smaller peaks from 1998-2001 and 2006-2010. After 2010, we can see a return to early 1950s numbers.

When I originally examined this plot, I was drawn to the dramatic drop in singles from 1991 to 1992. So I did more research and found an article published in the Washington Post that explained this dramatic decrease in number one singles:

__The Washington Post:__
<blockquote>
“When the Beatles were around, there were horrible records of who sold what,” Donald S. Passman, author of “All You Need to Know About the Music Business,” told The Washington Post. “Nobody knew how many records were sold in retail, only how many were shipped to the store. So the charts were based on shipments.”

Smelling opportunity, many record companies would simply send out a bunch of records. Even if they ended up getting half of them back, the albums would climb the charts.

As Steve Knopper — who recently added a chapter on the streaming age to his book “Appetite for Self-Destruction: The Spectacular Crash of the Record Industry in the Digital Age” — put it: “There was a lot of hanky-panky going on, with record labels lobbying the stores. In the old days in the record industry, there were a lot of interesting ways of goosing the charts.”

SoundScan, a technology for tracking music sales and airplay, appeared in 1991 like a sonic boom. Suddenly, the charts were being fed actual, reliable statistics.

“Can you say Kanye is as big an artist, being this successful in streaming, compared to Michael Jackson in the ’80s or the Beatles in the ’60s?” Knopper said. “That seems like apples and oranges. … It’s a completely different type of success and consumption.”
</blockquote>

[Source](https://www.washingtonpost.com/news/arts-and-entertainment/wp/2018/07/05/billboards-charts-used-to-be-our-barometer-for-music-success-are-they-meaningless-in-the-streaming-age/)

Basically, before SoundScan the Billboard charts were based solely on how many records were sent to record stores, not how many records ended up being sold. It appears there were more number one singles in the past because it was easier to game the system back then, but with accuracy being introduced into the charts, the rise of the streaming age, and the evolution of Billboard's algorithm, its difficult to compare the success of musicians by looking solely at the charts.

### 2. Which artists have the most number one singles?
Originally, I wanted to look at the top 10 acts with the most number one hits. Upon taking a closer look at the counts, I discovered that the 10th artist shares the spot with two other artists, which is why this part of the analysis looks at the top 12 artists with the most number one singles:

| Rank |     Artist      | Total Number Ones |
|------|-----------------|-------------------|
| 1    |   The Beatles   |       20          |
| 2    |   Mariah Carey  |       19          |
| 3    |  Elvis Presley  |       17          |
| 4    | Michael Jackson |       12          |
| 4    |     Madonna     |       12          |
| 5    | Whitney Houson  |       11          |
| 5    |     Rihanna     |       11          |
| 6    |  The Supremes   |       10          |
| 6    |  Janet Jackson  |       10          |
| 7    |    Bee Gees     |        9          |
| 7    |   Katy Perry    |        9          |
| 7    |     Usher       |        9          |       

The Beatles have had the most number one hits, while Mariah Carey trails them by just one song, and Elvis by 3. I did a quick Google search to verify the counts and each artist's position in the top 12.

One thing that caught me off guard was the artists in the top two positions. I know The Beatles were big in their time, and their music still popular today, but they were together for a short time relative to artists today. Mariah Carey is a great example of a more modern artist with a long career.

A quick search told me that The Beatles were actually together for 8 years and Mariah Carey has been making music since 1990. This led me to take a closer look at the length of time between each artist's first and last (or more recent) number one single. 

<img src="figures\static\top-artist-hits-by-year.png">

In the above plot, I've represented each artist's career as a histogram showing the amount of number one singles they've had, with the years between their first number one and their last number one as the x-axis.

From these plots, I was able to identify each artist's most productive years, as shown by the year(s) they had multiple number one hits. I was tempted to label these productive years as the period each artist peaked in their careers. However, music is subjective, and in my opinion, having several number one hits does not indicate music quality or maturity of an artist. Instead, I chose to refer to these peaks as each artist's peak commercial success.

It was interesting to see from the above plots, the amount of time it took each artist to accumulate enough hits to get them into the top 12.

The Supremes managed to get 10 number one hits in a span of 4 years, the shortest productive period of the top 12 artists. The Supremes are tied with Janet Jackson for the 6th spot in the list of top 12 artists with the most number one singles. Janet Jackson also has 10 number one hits, but accumulated them over 16 years, an extra 12 years than it took The Supremes.

It is tempting to conclude that artists that had more number ones over a shorter period of time were more successful than artists that took longer to accumulate their number ones. However, there are a lot of factors at play here that cannot necessarily be measured. Given what I know about some of the artists in the top 12, an artist's personal life, band/group/label dynamics, music executive demands, and the competitiveness of the music industry are possible reasons for the differences in commercial success.

### 3. Are songs that go number one sung more by women or men? Solo acts or ensembles/groups?
There was no way for me to feasibly identify the gender of each artist and whether or not they were a solo or group for the whole dataset. Instead, I'll answer this question with the artists in the top 12 for most number one singles.

Of the top 12 artists, 7 (58.3%) of them are female and 5 (41.6%) are male. Three of these acts are groups/ensembles, the 9 others are solo acts.

### 4. Of all songs that went number one since 1950, are there any commonalities between the songs? Like tempo, valence, etc. ?

I plotted the distributions of each feature in the dataset to answer this question.

<img src="figures\static\audio-feature-distributions.png">

Danceability, energy, loudness, and tempo are slightly left skewed. Speechiness, instrumentalness, liveness, and duration are heavily right-skewed, but this was expected based on what these features represent. Valence and acousticness were most interesting to me; I expected acousticness to be distributed similarly to instrumentalness, but it doesn't seem to be as skewed. Valence also had an interesting distribution as I expected it to be left-skewed, since valence here means how positive or happy a song sounds, and hit songs tend to be pretty upbeat unless they're ballads. However, I expected this distribution to resemble the danceability distribution, centered around 0.7-0.9.

### 5. Is there any trends among audio features? (i.e. Does tempo stay consisent among the decades, or does it exhibit some type of cyclical pattern?)

I aggregated each feature by decade and calculated the mean to get an idea of how each feature changed by the decade. 

<img src="figures\static\mean-audio-feature-decade.png">

Based on the danceability plot above, number one hits had a danceabilty score above 0.5. There's been a slight increasing trend since the 1950s of songs becoming more danceable as the decades have gone on. There is a similar trend in the energy plot.

The first rock and roll song went number one in 1955. Before that, songs in the 1950s were generally low energy, highly instrumental, and highly acoustic. Several artists of the early 1950s were accompanied by orchestras, some songs were even solely instrumental. After 1955, doo-wop, an early genre of R&B, started gaining popularity which was more vocal and incorporated little to no instrumentals. The drop in instrumentalness from 1950 to 1960 could be explained by the popularization of rock and roll.

Another interesting trend is the dramatic increase of speechiness in the 2000s compared to the 1990s. I imagine this can be attributed to the rising popularity of rap and hip-hop songs in the 90s, and the explosion of these two genres in the 2000s.

Tempo appears pretty steady throughout the decades, which is interesting because I would expect songs to become faster. Valence stays around the same levels as well. Looking at song duration, I see that songs in the 1950s were much shorter, with songs getting progressively longer through the 90s, and eventually decreasing again.

Loudness appears to become less negative, which I imagine means songs are getting louder as time goes on. This makes sense since [loudness was highly correlated with energy](notebooks\7-exploration-and-analysis.ipynb), which also increases with the decades.

### 6. Are genres consistent among number ones? Do all songs have similar genres?
When analyzing genres, I used genre tags assigned by Spotify. In some cases, songs are assigned a list of genres; in the tables below, genres consisting of "/" denote these genre lists. To retain the unique genres, I didn't perform any data cleaning on the `genres` column aside from populating null values. The counts below are each decade's top five genres.

__1950s:__

| Genre | Count |
|-------|-------|
| Pop   |   13  |
| Rock-and-Roll / Rockabilly | 12 |
| Easy Listening / Vocal Jazz / Lounge | 5 |
| Country | 5 |
| Vocal | 5 |
<br>
<p>
As I mentioned before, the 1950s saw the popularization of rock and roll. Almost all songs in this genre were by Elvis Presley. I see a genre referred to as easy listening. A quick search tells me that easy listening music is the type of music that preceded rock and roll, is melodic, accompanied by string instruments.

From Wikipedia:
>Easy listening music featured popular vocalists such as Perry Como, Frank Sinatra, Bing Crosby, Dean Martin, Tony Bennett, Dionne Warwick, Bill Kenny, Astrud Gilberto, Matt Monro, The Carpenters and many others.

[Source](https://en.wikipedia.org/wiki/Easy_listening)

This makes sense considering what I saw in the feature distributions for instrumentalness and energy. Artists in this genre include Tony Bennett, Doris Day, Dean Martin, and Perry Como. The vocal and country genres also make sense for this era of music. Country music at this time sounded fairly similar to pop music. Pop music was anything else that wasn't considered rock-and-roll.
</p>
<br>

__1960s:__

| Genre | Count |
|-------|-------|
| Rock   |   35  |
| R&B / Soul | 23 |
| Pop | 21 |
| Rock-and-Roll / Rockabilly | 6 |
| Easy Listening / Lounge | 4 |
<br>
<p>
In this decade, rock and r&b/soul overtook pop as the most popular genre. The beginnings of more modern rock begins in this decade with The Beatles, The Beach Boys, The Rolling Stones, and The Mamas & The Papas. The rise of r&b can be attributed to artists such as Ray Charles, and the groups coming from Motown: The Supremes, The Temptations, Mary Wells, Stevie Wonder. Pop music here is again, anything that isn't rock. It can be characterized as the vocal and doo-wop songs that became popular at the end of the 50s. In the 60s, these pop artists were Dion, Lesley Gore, and The Righteous Brothers. The six rock-and-roll songs were by Elvis.</p><br>

__1970s:__

| Genre | Count |
|-------|-------|
| Pop   |   40  |
| R&B / Soul | 30 |
| Rock | 27 |
| Soundtrack | 6 |
| Disco | 6 |
<br>
<p>With the 70s, pop music begins to encompass several genres and acts from artists of the previous decades, as opposed to previous decades where the pop genre was much less diverse. I imagine this is why pop becomes the most common genre among number ones in this decade. In the 70s, rock (George Harrison, Linda Ronstadt), r&b (Marvin Gaye) and several disco artists (BeeGees, ABBA) make up the pop genre. This decade also sees the rise of disco and an increasingly diverse rock genre influenced by the rock artists of the decade prior.</p><br>

__1980s:__

| Genre | Count |
|-------|-------|
| Rock   |   32  |
| Pop | 20 |
| R&B / Soul | 9 |
| Pop / R&B / Soul | 8 |
| Dance Pop | 7 |
<br>
<p>In the 1980s, disco ends and r&b is on the decline compared to the decade before. As in the 60s, rock overtakes pop as the most popular genre for number one songs. The genres that are popular in the 80s are very similar to genres of the previous decades, but the sounds and artists that make up these genres starts to become more diverse. The rock genre also becomes more diverse, incorporating great rock artists of the previous decades (Paul McCartney, Queen, Boston, Heart) with newer artists and sounds from bands such as Bon Jovi and Billy Idol. This decade launches the careers of several more modern artists that would go on to still be making music today, 40 years later. We see the launch of Michael Jackson's solo career. Dance pop also becomes very popular in this decade thanks to Madonna and Whitney Houston.</p><br>

__1990s:__

| Genre | Count |
|-------|-------|
| Pop   |   24  |
| Dance Pop / R&B / Urban Contemporary | 14 |
| R&B / Soul | 9 |
| Dance Pop | 4 |
| Hip-Hop / Rap | 4 |
<br>
<p>Dance pop continues to be popular into the 90s, and pop music becomes the top genre of this decade. This decade is exciting because hip-hop and rap start to become popularized and start to reach number one, despite hip-hop and rap having been around since the 1970s. The first "official" popular rap song, Rapper's Delight, charted in 1979 but did not go number one. Interestingly, rock is in heavy decline during this decade. Only 4 rock songs went number one, and they were all at the beginning of the decade.</p><br>

__2000s:__

| Genre | Count |
|-------|-------|
| Hip-Hop / Rap  |   25  |
| Pop | 16 |
| Hip-Hop / Dance Pop / R&B | 7 |
| Dance Pop / Post-Teen Pop | 6 |
| R&B / Soul | 5 |
<br>
<p>If the 90s popularized hip-hop and rap music, then the 2000s is when this genre flourished. In this decade, hip-hop/rap was the most popular genre, having at least 32 songs go number one. Dance pop starts to decline in this decade. Pop again is the second most popular genre. The decline of rock music continues, in the 2000s only one rock song goes number one, "With Arms Wide Open" by Creed.</p><br>

__2010s:__

| Genre | Count |
|-------|-------|
| Pop   |  36   |
| Hip-Hop / Rap | 14 |
| Dance Pop | 7 |
| Alternative | 5 |
| Dance Pop / Post-Teen Pop  | 4 |
<br>
<p>Pop once again becomes the most popular genre, however, as stated before, it encompasses several different genres and references music that is popular. Hip-hop and rap continue to be popular and dance pop starts to rise again. As rock declined in the previous decades, a new subgenre of rock rises in the 2010s, alternative rock. This genre is made up by artists such as Lorde and Billie Eilish.</p><br>

__Overview:__
 Genres in the 2000s and 2010s start to become blurred as pop music becomes more diverse and music becomes more experimental. It appears that genres over the decades have changed as new and different styles are introduced and become popular. For example, rock music was the top genre in the 60s but when it became the top genre again in the 80s, it sounded very different. For some perspective, The Beatles, The Rolling Stones, and The Beach Boys were the top rock groups of the 1960s, and in the 80s, the top rock groups were Bon Jovi, Paul McCartney, and Huey Lewis & The News.
 
 So it's difficult to say whether a genre has really "endured" through the decades, but we can definitely see which genres were popular during these times and how they've changed.

### 7. Are songs in each decade distinct? Specifically, are songs in each decade statistically different than the others?

I decided to answer this question by looking at `danceability`, `energy`, and `valence` across the decades. I chose these three features because the trends were not as dramatic, and because I feel they represent qualities that a number one song would possess: danceable, high energy, and positive sounding. There appeared to be an increasing trend in danceability and energy over time. Valence appeared to increase from the 50s through the 70s, and decrease until present.

First, I wanted to run a statistical test to compare the mean danceability, energy, and valence for each decade, and whether or not their means are equal. I hypothesized at least one decade would have a different mean than the others. Specifically, at least one decade's danceability, energy, or valence would be unique.

Then, I wanted to run a pairwise test to see which decades are statistically different from each other for each feature.

#### __Running the Tests__
Since the songs, my samples in this case, did not come from a normally distributed population, I decided to run non-parametric tests. I used the Kruskal-Wallis H-Test to determine whether more than two decades have different distributions for each feature. My null and alternative hypotheses were:

$H_0$: Sample feature distributions are equal across all decades.

$H_A$: One or more decade's sample feature distributions are not equal.

The results of the Kruskal-Wallis test, with a 0.05 alpha level, were:

| Feature | p-value | Reject? |
|---------|---------|---------|
|danceability| ~ 0.0 | Yes |
|energy | ~ 0.0 | Yes |
|valence| ~ 0.0 | Yes |

<br>
For each feature, I rejected the null and accepted the alternative hypothesis that at least one decade had a danceability, energy, and valence distribution that is not equal to the others.

Then, I used Dunn's Test to pinpoint which decade's means are significant from the others. My null and alternative hypotheses were:

$H_0$: There is no difference in sample feature distributions between decades.

$H_A$: There is a difference in sample feature distributions between decades.

The results of Dunn's Test, with a 0.05 alpha level, are shown in the plot below. The top row shows the pairwise p-values for each decade pair as a heatmap, where colored cells denote decades where that is a difference in feature distributions. The bottom row shows the trend of each feature's mean over time, and serves as a reference for the heatmaps above it.

<img src="figures\static\test-result-plots.png">

__Danceability:__

The results of testing danceability showed that consecutive decades are not statistically different from each other with one exception. For example, danceability is not statistically different between the 1950s and 1960s, the 1970s and 1980s, and so on. The exception is the significant difference between the 1960s and 1970s. Looking at the line plot of mean danceability, verified these findings. The increasing trend is gradual and only varies between a mean of 0.5 to 0,7; changes between the decades are relatively small.

__Energy:__

The difference in energy between every other decade appears to be statistically significant: 50s and 60s, 70s and 80s, 90s and 00s. By this trend, the following decade pairs are not statistically different: 60s and 70s, 80s and 90s, 00s and 10s. This kind of trend appears to make some sense given the line plot of mean energy. Energy is increasing overall, but there are some consecutive decades where there is a deacrease, or energy doesn't change enough to be statistically significant.

__Valence:__

Mean valence, like danceability, only varies over a small range of values. The means range between 0.55 and about 0.78, which may be the reason there is few pairwise relationships that are statistically significant. For example, the 1950s are only different from the 1960s and 1970s; after the 70s, valence varies between ~0.55 and 0.6. There doesn't appear to be an overall trend since valence increases or decreases between decades. Most of the difference in valence is seen in the 1960s and 70s, since this period had a higher mean valence compared to the other decades.

## Conclusion

The questions I posed at the beginning of my analysis focused on identifying trends and comparing music from the last 70 years. I've found that while some valid comparisons can be made, others cannot.

Due to poor record keeping in the 50s to 60s, inconsistencies of Billboard's charting algorithm, the implementation of SoundScan in the early 90s, and changes in the way we listen to music, it would be difficult to conduct an analysis comparing the success of music across the decades.

However, it is possible to compare the music itself and identify how music styles have changed over time.