import tweepy
import csv

# didapat dari akun developer twitter
access_token = "1162392652345556994-V5tLm6bWKFR3CiF01jvHsC1EFgwnuZ"
access_token_secret = "oZl7fwzACpN0bUHc9wrQm2LtPRyu9CE7KtppOdLysX69l"
api_key = "alvfmX4iSxY4d22d7hie35gBo"
api_key_secret = "JVYkGRC0gKrHZ06a0hcXMkKRYz3xFaz6YgyYJpNL1jWHspYDyo"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# membuka/membuat file untuk menambahkan data
csvFile = open('list_tweets.csv', 'w', encoding='utf-8')
# gunakan csv writer untuk menulis data
csvWriter = csv.writer(csvFile)

# mencari data berdasarkan keyword
hasilsearch = api.search_tweets(q="kuliner nusantara", tweet_mode="extended",
                                lang="id", since="2020-01-01", until="2022-05-23", count=200)
# mencari data berdasarkan Akun
hasiluser = api.user_timeline(id="Lambe_Turah", tweet_mode="extended",
                              lang="id", since="2020-01-01", until="2022-05-23", count=400)

for tweets in hasiluser:
    text = tweets.full_text
    user = tweets.user.name
    created = tweets.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()
