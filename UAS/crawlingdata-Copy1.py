#!/usr/bin/env python
# coding: utf-8

# In[43]:


from time import time
import snscrape.modules.twitter as sntwitter
import pandas as pd
import emoji
import contractions
import re

query = input("Masukkan keyword yang ingin dicari: ")  # menu untuk memasukkan kata kunci
since = input("Masukkan tanggal awal pencarian:")
until = input("Masukkan tanggal akhir pencarian:")
tweets = []
limit = 1000  # jumlah tweet yang ingin diambil

for tweet in sntwitter.TwitterSearchScraper(query=query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
df = pd.DataFrame(tweets, columns=['Time', 'Username', 'Tweet'])
df


# In[64]:


def cleansing(tweet):
    # Replace RT tag
    t1 = re.sub('RT\s', '', tweet)
    # Replace @_username
    t2 = re.sub('\B@\w+', "", t1)
    # Replace emojis with text
    t3 = emoji.demojize(t2)
    # Replace URL (http:// or https://)
    t4 = re.sub('(http|https):\/\/\S+', '', t3)
    # Replace #_something_
    t5 = re.sub('#+', '', t4)
    # Lower case each letter
    t6 = t5.lower()
    # Replace word repetition with a single occurance ('ooooooooo' becomse 'oo')
    t7 = re.sub(r'(.)\1+', r'\1\1', t6)
    # Replace punctuation repetition with a single occurance ('!!!!!!!!' becomes '!')
    t8 = re.sub(r'[\?\.\!]+(?=[\?.\!])', '', t7)
    # Alphabets only, exlude numbers and special characters
    t9 = re.sub(r'[^a-zA-Z]', ' ', t8)
    # Replace contractions with their extended forms
    t10 = contractions.fix(t9)
    return t10


# In[65]:


for i, r in df.iterrows():
    y = cleansing(r['Tweet'])
    df.loc[i, 'Tweet'] = y
df

# In[ ]:
