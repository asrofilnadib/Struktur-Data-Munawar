import sys
from CrawlingTwitter import CrawlTwitter


class Menu(object):
    """memunculkan menu dan merespon untuk memilih menjalankan perintah apa"""

    def __init__(self):
        self.crawling = CrawlTwitter()
        self.choice = {
            "1": self.crawling_tweets,
            "2": self.show_crawler,
            # "3": self.graphics,
            "4": self.quit
        }

    def display_menu(self):
        print("""
        Crawling Menu

        1. Crawling data Tweets
        2. Hasil dari Crawl data
        3. Menampilkan Crawling Dalam Bentuk Graphics
        4. Quit
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
        tweets = []
        try:
            mengambilTweets = CrawlTwitter().crawling_data()

            for tweet in mengambilTweets:
                parsedTweet = {'text': tweet.full_text}
                if tweet.retweet_count > 0:
                    if parsedTweet not in tweets:
                        tweets.append(parsedTweet)
                else:
                    tweets.append(parsedTweet)
            return tweets
        except Exception as e:
            print("Error: " + str(e))

    def cleansing(self):

    def show_crawler(self):
        x = self.crawling.crawling_data()
        return x

    # def graphics(self):

    def quit(self):
        '''perintah untuk keluar dari program'''
        print("Terima Kasih telah menggunakan program ini")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
