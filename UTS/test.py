import tweepy
import csv

api_key = "uSY64ZyoniWb1luJQO4wZtlXg"
api_key_secret = "cDKD3MEOufdI95Hw3C88z2vxJ8hgYVPUIvs3yzOeLGHveUV2K5"

access_token = "1528619269189410816-fJKEWur1obiYmOTIyaYCdvZUpQu60v"
access_token_secret = "aB8tLzOGRpX8GNDvqh9sYMbtpbrOndBJ9GW1QAxsx0q7w"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# q merupakan kata kunci yang ingin di cari di twitter

csvFile = open('list_tweets.csv', 'w', encoding='utf-8')
csvWriter = csv.writer(csvFile)

public_tweets = api.search_tweets(q="jokowi dodo", tweet_mode="extended",
                                  lang="id", since="2020-01-01", until="2022-06-14", count=500)

for tweets in public_tweets:
    text = tweets.full_text
    user = tweets.user.name
    created = tweets.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()