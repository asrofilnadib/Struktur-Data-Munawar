import csv
import sys
import tweepy
import matplotlib.pyplot as plt

from Crawler import CrawlingTwitter


class Menu(object):
    """memunculkan menu dan merespon untuk memilih menjalankan perintah apa"""
    def __init__(self):
        self.crawling = CrawlingTwitter()
        self.choice = {
            "1": self.crawling_tweets,
            "2": self.show_crawler,
            "3": self.graphics,
            "4": self.cleansing,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Crawling Menu
        
        1. Crawling data Tweets
        2. Hasil dari Crawl data
        3. Menampilkan Crawling Dalam Bentuk Graphics
        4. Cleansing dan normalization
        5. Quit
        """)

    def run(self):
        """memunculkan menu dan merespon untuk memilih"""
        while True:
            self.display_menu()
            choice = input("Masukan opsi anda: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} tidak valid dengan opsi".format(choice))

    def crawling_tweets(self):
        """memerintahkan metode yang ada pada kelas CrawlingTwitter dalam
        module Crawler untuk mengambil data tweets"""
        tweets = []
        try:
            mengambilTweets = CrawlingTwitter().crawlingTweets()

            for tweet in mengambilTweets:
                parsedTweet = {'text': tweet.full_text}
                if tweet.retweet_count > 0:
                    if parsedTweet not in tweets:
                        tweets.append(parsedTweet)
                else:
                    tweets.append(parsedTweet)
            return tweets
        except tweepy.TweepyException as e:
            print("Error: " + str(e))

    def show_crawler(self):
        """memunculkan hasil crawling data langsung di terminal"""
        with open('crawl_tweets.csv', 'r', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            for rows in reader:
                print(rows)
        csvFile.close()

    def graphics(self):
        """membuat graphic untuk memvisualisasikan data crawling"""
        x = []

        with open("crawl_tweets.csv", "r", encoding="utf-8") as csvFile:
            line = csv.reader(csvFile, delimiter=',')
            for rows in line:
                x.append(int(rows[1]))

            plt.plot(x, color='g', linestyle='dashed', marker='0',
                     label='crawling data')

            plt.xticks(rotation=25)
            plt.xlabel('Tanggal')
            plt.title("Crawling Data")
            plt.grid()
            plt.legend()
            plt.show()
        csvFile.close()


    def quit(self):
        '''perintah untuk keluar dari program'''
        print("Terima Kasih telah menggunakan program ini")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
