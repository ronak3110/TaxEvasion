from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


ckey = "q9vjzhnJZmEKfHpLwCMsGfJCE"
csecret = "gSX0omiVviHxyO5MV0LrKOzIV3O0zRbE56n0ucb4QpRKjIszYd"
atoken = "933415947276206080-sdyZ9CPqZfsqHN3ngYww0rUw2dnel0d"
asecret = "Y30c3tVcvd70IhgbvUyUExM5UHDfKg9QT4EGaz6i5OZHC"

from twitterapistuff import *

class listener(StreamListener):

    def on_data(self,data):
        all_data = jason.loads(data)
        tweet = all_data["text"]
        sentiment_value,confidence = s.sentiment(tweet)
        print(tweet,sentiment_value,confidence)

        if confidence*100 >=80:
            output = open("twitter-out.txt",'a')
            output.write(sentiment_value)
            output.write("\n")
            output.close()
        return True

    def on_error(self,data):
        print(status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["tax"])
