import json
import requests
import tweepy
from bs4 import BeautifulSoup
import re

consumer_key = "JauYlvETfEHaBmyJhVpHeY2k8"
consumer_secret = "0sU7tQiNfBb5lm8rDclXH78mDCNxJskaf4i0k9Q0XlsJoYGwxR"
access_token = "1094173736129855488-5L8M2juPyAbalGjSE1GesU8paJRNBw"
access_token_secret = "mn8dIvJLu8fJ9a6DhTfq7YI85RDlKV0tDFrXvG6ttldUS"

file_count = 0


# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):
    def on_connect(self):
        print("You are connected to Twitter API")

    def on_error(self, status_code):
        if status_code != 200:
            print("error found")
            # returning false disconnects streams
            return False

    """ 
    This method reads in tweet data as json and extracts the data we want
    """

    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)
            if "text" in data:
                # created_at = parse(data['created_at'])
                # created_at = data["created_at"]
                tweet = data["text"]
                # remove html tags
                tweet = BeautifulSoup(tweet, 'lxml').get_text()
                response = requests.get(f"https://sentiment-analyzer-api.herokuapp.com/analyzer/predict/{tweet}")
                # print(response.content)
                if response.status_code == 200:
                    global file_count
                    file_count += 1
                    # print(tweet)

                    score = response.text.split(":")
                    score_cleaned = score[-1].replace("}", "")

                    with open(f"sitedata/twitter/score/{file_count}.txt", "w") as writer:
                        writer.write(f"{score_cleaned}")

                    with open(f"sitedata/twitter/tweet/{file_count}.txt", "w") as writer:
                        writer.write(f"{tweet.encode('utf8')}")

                # elif response.status_code == 404:
                # print('Not Found.')

        except EnvironmentError as e:
            print(e)


class ExtractTweet:
    def extract_tweet(self, track):
        # authentification so we can access twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        # create instance of Streamlistener
        listener = Streamlistener(api=api)
        stream = tweepy.Stream(auth, listener=listener)

        track = [track]

        # choose what we want to filter by
        stream.filter(track=track, languages=['en', 'fil'], filter_level='medium')

    def stop_stream(self):
        global file_count
        file_count = 0
