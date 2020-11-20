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

I expected more recent decades to have the most number one singles due to the amount of music diversity there is. However, it appears the 1970s had the most number one singles. The histogram above also shows an increasing trend in the amount of number one single from the 50s through the 70s. The amount of number one singles first starts in decrease in the 1980s, and continues this decreasing trend until today. 

I was curious about this decrease in singles and found an article from NME:

__NME: The number of unique Number One singles is decreasing.__
<blockquote>
In the ‘70s, the average number of Number Ones could be as high as 30 per year. In the past four years we haven’t had more than 13 unique Number Ones per year. As BBC Radio 1 boss Chris Price explained to NME last year, the stagnancy of the chart is probably down to streaming being counted in the charts:

“We’ve moved away from somebody walking into HMV and being a physical single, or downloading a 99p download from iTunes, and we’re moving much more towards measuring engagement over time. It’s less like somebody walking into a shop and making a purchase, and more like somebody sitting at home in their bedroom and listening to something several times over.”
</blockquote>

[Source](https://www.nme.com/blogs/nme-blogs/billboard-100-shorter-explicit-2054269)  

The way we've started to listen to music has contributed to a drop in the amount of songs that go number one. After finding this out, I was interested in whether I coult pinpoint a specific year for this drop in number one hits, so I aggegated the counts by year to see the total songs that went number one in each year from 1950 to present.

<img src="figures\static\number-one-counts-year.png">

From the plot above, there are 3 major peaks in the amount of number ones per year. The first peak in the mid 60s, the mid 70s, and a persistent peak that started in the mid 80s and lasted through the early 90s. There are some smaller peaks from 1998-2001 and 2006-2010. After 2010, we can see a return to early 1950s numbers.

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

Basically, before SoundScan the Billboard charts were based solely on how many records were sent to record stores, not how many records ended up being sold.Chart manipulation was also rampant. It appears there were more number one singles in the past because it was easier to game the system back then, but with accuracy being introduced into the charts, the rise of the streaming age, and the evolution of Billboard's algorithm, its difficult to compare the success of musicians by looking solely at the charts.

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

The Supremes managed to get 10 number one hits in a span of 4 years, the shortest productive period of the top 12 artists. The Supremes are tied with Janet Jackson for the 6th spot in the list of top hit makers. Janet Jackson also has 10 number one hits, but accumulated them over 16 years, an extra 12 years than it took The Supremes.

However, there are a lot of factors at play here that cannot necessarily be measured. Given what I know about some of the artists in the top 12, an artist's personal life, band/group dynamics, desires of music executives, and the competitiveness of the music industry are possible reasons for the contrast.

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

Before 1955, when the first rock and roll song went number one, songs in the 1950s were generally low energy, highly instrumental, and highly acoustic. Several artists of the early 1950s were accompanied by orchestras, some songs were even solely instrumental. The latter half of the decade sees the rise of doo-wop, an early genre of R&B, which was more vocal and incorporated little to no instrumentals. Doo-wop as a genre typically characterizes the musical style of this decade.

Another interesting trend is the dramatic increase of speechiness in the 2000s compared to the 1990s. I imagine this can be attributed to the rising popularity of rap/hip-hop songs in the 90s, then the explosion of these two genres in the 2000s.

Tempo appears pretty steady throughout the decades, which is interesting because I would expect songs to become faster. Valence stays around the same levels as well. Looking at song duration, I see that songs in the 1950s were much shorter, with songs getting progressively longer through the 90s, and eventually decreaseing again.

Loudness appears to become less negative, which I imagine means songs are getting louder as time goes on. This makes sense since loudness was highly correlated with energy, which also increases with the decades.