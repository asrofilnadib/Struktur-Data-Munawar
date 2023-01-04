import tweepy
import csv
# import re
# import emoji
# import contractions


class CrawlingTwitter(object):
    def __init__(self):
        """Mendapatkan hak akses dari API twitter"""
        self.df = None
        api_key = 'Iu6lY3BLMIftN9KQTgpAIVgML'
        api_key_secret = 'HHcnvWracQjDiHNFc1KBF7SFNB5drN2pmzTztmEPAEmNndPC8k'
        access_token = '1162392652345556994-6V4BuMdmCQRd2zL4XEoHHEagsd8bR5'
        access_token_secret = '80pT9q3h5cDu6j0VzxzeukloefPplG8fknrOLlawulCob'

        try:
            self.auth = tweepy.OAuthHandler(api_key, api_key_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def crawlingTweets(self):
        """membuka lalu menulis pada file csv,
        menarik/crawling data tweets dari twitter melalui API twitter,
        hasil dari data tweets yang sudah dicrawling tadi
        ditulis ke dalam file csv lalu file ditutup"""
        csvFile = open('crawl_tweets.csv', 'w', encoding="utf-8")
        csvWriter = csv.writer(csvFile)

        q = str(input("Konteks Tweet: "))
        hasilsearch = self.api.search_tweets(q, tweet_mode="extended", lang="id", count=1000)

        self.tweepy_copy = []
        for tweets in hasilsearch:
            self.tweepy_copy.append(tweets)

        for tweets in hasilsearch:
            text = tweets.full_text
            user = tweets.user.name
            created = tweets.created_at
            csvWriter.writerow([created, user, text.encode('utf-8')])
        csvWriter = csv.writer(csvFile)
        csvFile.close()

        return hasilsearch

    # def cleansing(self, tweet):
    #     # Replace RT tag
    #     t1 = re.sub('RT\s', '', tweet)
    #     # Replace @_username
    #     t2 = re.sub('\B@\w+', "", t1)
    #     # Replace emojis with text
    #     t3 = emoji.demojize(t2)
    #     # Replace URL (http:// or https://)
    #     t4 = re.sub('(http|https):\/\/\S+', '', t3)
    #     # Replace #_something_
    #     t5 = re.sub('#+', '', t4)
    #     # Lower case each letter
    #     t6 = t5.lower()
    #     # Replace word repetition with a single occurance ('ooooooooo' becomse 'oo')
    #     t7 = re.sub(r'(.)\1+', r'\1\1', t6)
    #     # Replace punctuation repetition with a single occurance ('!!!!!!!!' becomes '!')
    #     t8 = re.sub(r'[\?\.\!]+(?=[\?.\!])', '', t7)
    #     # Alphabets only, exlude numbers and special characters
    #     t9 = re.sub(r'[^a-zA-Z]', ' ', t8)
    #     # Replace contractions with their extended forms
    #     t10 = contractions.fix(t9)
    #     return t10
    #
    # def outclean(self):
    #     for i, r in self.df.iterrows():
    #         y = CrawlingTwitter.cleansing(r['Tweet'])
    #         self.df.loc[i, 'Tweet'] = y
    #     return self.df
