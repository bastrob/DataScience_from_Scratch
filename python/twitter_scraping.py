# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:57:22 2020

@author: Bast
"""

import os


CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")

import webbrowser
from twython import Twython

# Get a temporary client to retrieve an authetification URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds["auth_url"]

# Now visit that URL to authorize the application and get a PIN
print(f"go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")

# Now we use that PIN_CODE to get tha actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds["oauth_token"],
                      temp_creds["oauth_token_secret"])

final_step = auth_client.get_authentication_tokens(PIN_CODE)
ACCESS_TOKEN = final_step["oauth_token"]
ACCESS_TOKEN_SECRET = final_step["oauth_token_secret"]

# And get a new Twython instance using them
twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)

# Save ACCESS_TOKEN & SECRET os


for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(f"{user}: {text}\n")
    

# Access the stream API

from twython import TwythonStreamer
from Collection import Counter


# Appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        """
        What do we do when Twitter sends us data?
        Here data will be a Python dict representing a tweet

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        # We only want to collect English-language tweets:
        if data.get("lang") == "en":
            tweets.append(data)
            print(f"received tweet #{len(tweets)}")
        
        if len(tweets) >= 100:
            self.disconnect()
        
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# start consuming public statuses that contain the keyword 'data'
stream.statuse.filter(track="data")

# if instead we wanted to start we wanted to start consuming a sample of *all* public statuses
# stream.statuses.sample()

top_hashtags = Counter(hashtag["text"].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])

print(top_hashtags.most_common(5))
