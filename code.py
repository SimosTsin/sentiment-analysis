# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:54:51 2019

@author: simos
"""

from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import regex as re


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

searchTerm = input("Enter term to search about: ")
no_of_searchTerms = int(input("Enter how many tweets to analyze: "))

# Constructing the database and populate it with tweets.
import sqlite3
conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS tweets_info(
        id INTEGER PRIMARY KEY,
        word TEXT,
        user TEXT,
        followers INTEGER, 
        tweets INTEGER, 
        retweets INTEGER,
        or_text TEXT,
        pr_text TEXT, 
        date TEXT, 
        loc TEXT, 
        hashtag TEXT,
        polarity NUMBER)""")
conn.commit()
   
def data_entry():
    c.execute("INSERT INTO tweets_info (word, user, followers, tweets, retweets, or_text, pr_text, date, loc, hashtag, polarity) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
              (searchTerm, username, no_followers, no_tweets, no_retweets, tweet_text, proc_text, datestamp, location, hashtags, polarity))
    conn.commit()
    
tweets =  tweepy.Cursor(api.search, q=searchTerm, until="2019-01-23", lang='en',tweet_mode='extended').items(no_of_searchTerms)
for tweet in tweets:
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        user = api.get_user('tweet')
        username=tweet.user.screen_name.lower()
        no_followers=tweet.user.followers_count
        no_tweets=tweet.user.statuses_count
        no_retweets=tweet.retweet_count
        tweet_text=tweet.full_text
        proc_text = re.sub('RT @[\w_]+: ', '', tweet_text)
        proc_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_text).split()).lower()
        datestamp=str(tweet.created_at)
        location=tweet.user.location.lower()
        hashtags=re.findall(r"#(\w+)",tweet.full_text)
        hashtags=','.join(hashtags).lower()
        analysis = TextBlob(proc_text)
        polarity = analysis.sentiment.polarity
        data_entry()
    else:
        continue


# Get the sentiment
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-16 %%'")
ts_16 = c.fetchall()
ts_16 = [i[0] for i in ts_16]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-17 %%'")
ts_17 = c.fetchall()
ts_17 = [i[0] for i in ts_17]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-18 %%'")
ts_18 = c.fetchall()
ts_18 = [i[0] for i in ts_18]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-19 %%'")
ts_19 = c.fetchall()
ts_19 = [i[0] for i in ts_19]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-20 %%'")
ts_20 = c.fetchall()
ts_20 = [i[0] for i in ts_20]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-21 %%'")
ts_21 = c.fetchall()
ts_21 = [i[0] for i in ts_21]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'tsitsipas' AND date LIKE '2019-01-22 %%'")
ts_22 = c.fetchall()
ts_22 = [i[0] for i in ts_22]


c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-16 %%'")
fe_16 = c.fetchall()
fe_16 = [i[0] for i in fe_16]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-17 %%'")
fe_17 = c.fetchall()
fe_17 = [i[0] for i in fe_17]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-18 %%'")
fe_18 = c.fetchall()
fe_18 = [i[0] for i in fe_18]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-19 %%'")
fe_19 = c.fetchall()
fe_19 = [i[0] for i in fe_19]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-20 %%'")
fe_20 = c.fetchall()
fe_20 = [i[0] for i in fe_20]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-21 %%'")
fe_21 = c.fetchall()
fe_21 = [i[0] for i in fe_21]
c.execute("SELECT polarity FROM tweets_info WHERE word = 'federer' AND date LIKE '2019-01-22 %%'")
fe_22 = c.fetchall()
fe_22 = [i[0] for i in fe_22]


total_ts = ts_16+ts_17+ts_18+ts_19+ts_20+ts_21+ts_22
len_total_ts = len(total_ts)
total_fe = fe_16+fe_17+fe_18+fe_19+fe_20+fe_21+fe_22
len_total_fe = len(total_fe)


# Making Dictionaries
ts = {'ts_16':ts_16,'ts_17':ts_17,'ts_18':ts_18,'ts_19':ts_19,'ts_20':ts_20,'ts_21':ts_21,'ts_22':ts_22}
fe = {'fe_16':fe_16,'fe_17':fe_17,'fe_18':fe_18,'fe_19':fe_19,'fe_20':fe_20,'fe_21':fe_21,'fe_22':fe_22}
ts_len = {k:len(v) for k,v in ts.items()}
fe_len = {k:len(v) for k,v in fe.items()}
ts_sentiment = {k:sum(v)/len(v) for k,v in ts.items()}
fe_sentiment = {k:sum(v)/len(v) for k,v in fe.items()}


ts_positive = []
ts_negative = []
ts_neutral = []

def ts_counter(x):
    positive = 0
    negative = 0
    neutral = 0
    for i in x:
        if (i == 0):
            neutral += 1
        elif (i < 0.00):
            negative += 1
        elif (i > 0.00):
            positive += 1

    return(ts_positive.insert(0,positive),ts_negative.insert(0,negative),ts_neutral.insert(0,neutral))
    
ts_counter(ts_22)
ts_counter(ts_21)
ts_counter(ts_20)
ts_counter(ts_19)
ts_counter(ts_18)
ts_counter(ts_17)
ts_counter(ts_16)

fe_positive = []
fe_negative = []
fe_neutral = []

def fe_counter(x):
    positive = 0
    negative = 0
    neutral = 0
    for i in x:
        if (i == 0):
            neutral += 1
        elif (i < 0.00):
            negative += 1
        elif (i > 0.00):
            positive += 1

    return(fe_positive.insert(0,positive),fe_negative.insert(0,negative),fe_neutral.insert(0,neutral))
    
fe_counter(fe_22)
fe_counter(fe_21)
fe_counter(fe_20)
fe_counter(fe_19)
fe_counter(fe_18)
fe_counter(fe_17)
fe_counter(fe_16)


c.close()
conn.close()

# Graphs
# Bar chart compering
import numpy as np

# Tsitsipas
n_groups = 7
 
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, ts_positive, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Positive')
 
rects2 = plt.bar(index + bar_width, ts_negative, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Negative')

rects3 = plt.bar(index + bar_width + bar_width, ts_neutral, bar_width,
                 alpha=opacity,
                 color='y',
                 label='Neutral')
 
plt.xlabel('January 2019')
plt.ylabel('Number of tweets')
plt.title("""Polarity by number of tweets
          between January 16th 2019 and January 22nd 2019 for Stefanos Tsitsipas""")
plt.xticks(index + bar_width , ('16', '17', '18', '19', '20', '21', '22'))
plt.legend()
 
plt.tight_layout()
plt.show()

# Federer
n_groups = 7
 
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, fe_positive, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Positive')
 
rects2 = plt.bar(index + bar_width, fe_negative, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Negative')

rects3 = plt.bar(index + bar_width + bar_width, fe_neutral, bar_width,
                 alpha=opacity,
                 color='y',
                 label='Neutral')
 
plt.xlabel('January 2019')
plt.ylabel('Number of tweets')
plt.title("""Polarity by number of tweets between 
          January 16th 2019 and January 22nd 2019 for Roger Federer""")
plt.xticks(index + bar_width, ('16', '17', '18', '19', '20', '21', '22'))
plt.legend()
 
plt.tight_layout()
plt.show()

# Total tweets for both
n_groups = 2
t_positive = [sum(ts_positive),sum(fe_positive)]
t_negative = [sum(ts_negative),sum(fe_negative)]
t_neutral = [sum(ts_neutral),sum(fe_neutral)]
 
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, t_positive, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Positive')
 
rects2 = plt.bar(index + bar_width, t_negative, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Negative')

rects3 = plt.bar(index + bar_width + bar_width, t_neutral, bar_width,
                 alpha=opacity,
                 color='y',
                 label='Neutral')
 
plt.xlabel('Person')
plt.ylabel('Number of tweets')
plt.title("""Polarity by number of tweets""")
plt.xticks(index + bar_width, ('Stefanos Tsitsipas', 'Roger Federer'))
plt.legend()
 
plt.tight_layout()
plt.show()

# Line chart with 2 lines

x_labels = ['Jan-16','Jan-17','Jan-18','Jan-19','Jan-20','Jan-21','Jan-22']
ts_sent = list(ts_sentiment.values())
fe_sent = list(fe_sentiment.values())
plt.plot(ts_sent, marker='', color='blue', linewidth=2, label="Stefanos Tsitsipas")
plt.plot(fe_sent, marker='', color='red', linewidth=2, label="Roger Federer")
plt.title('Sentiment per day')
plt.xlabel('timeline')
plt.ylabel('sentiment')
plt.xticks(np.arange(len(x_labels)), x_labels, rotation=0)
plt.grid(True)
plt.legend()
plt.show()

