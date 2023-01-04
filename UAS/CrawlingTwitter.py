from time import time
import snscrape.modules.twitter as sntwitter
import pandas as pd
import emoji
import contractions
import re


class CrawlTwitter(object):
    def __init__(self, query='', since='', until='', **kwargs):
        super().__init__(**kwargs)
        self.df = None
        self.query = query
        self.since = since
        self.until = until

    def crawling_data(self):
        self.query = input("Masukkan keyword yang ingin dicari: ")  # menu untuk memasukkan kata kunci
        self.since = input("Masukkan tanggal awal pencarian (YY-MM-DD):")
        self.until = input("Masukkan tanggal akhir pencarian (YY-MM-DD):")
        tweets = []
        self.limit = 1000  # jumlah tweet yang ingin diambil

        for tweet in sntwitter.TwitterSearchScraper(query=self.query).get_items():
            if len(tweets) == self.limit:
                break
            else:
                tweets.append([tweet.date, tweet.user.username, tweet.content])
        self.df = pd.DataFrame(tweets, columns=['Time', 'Username', 'Tweet'])
        self.df.to_csv("crawling a tweets.csv", index=False)
        return self.df

    def cleansing(self, tweet):
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

    def outclean(self):
        for i, r in self.df.iterrows():
            y = CrawlTwitter.cleansing(r['Tweet'])
            self.df.loc[i, 'Tweet'] = y
        return self.df