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

<img style="float: right;" src="figures\static\number-one-counts-decade.png">

I expected more recent decades to have the most number one singles due to the amount of music diversity there is. However, it appears the 1970s had the most number one singles. The histogram above also shows an increasing trend in the amount of number one single from the 50s through the 70s. The amount of number one singles first starts in decrease in the 1980s, and continues this decreasing trend until today.



