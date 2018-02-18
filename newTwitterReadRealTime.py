from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import predictionModule as pm


ckey = "q9vjzhnJZmEKfHpLwCMsGfJCE"
csecret = "gSX0omiVviHxyO5MV0LrKOzIV3O0zRbE56n0ucb4QpRKjIszYd"
atoken = "933415947276206080-sdyZ9CPqZfsqHN3ngYww0rUw2dnel0d"
asecret = "Y30c3tVcvd70IhgbvUyUExM5UHDfKg9QT4EGaz6i5OZHC"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            
            tweet = all_data["text"]
            val , conf = pm.predictThis(tweet)
            print(tweet, val )
            
            if conf*100 >=80:
                output = open('twitter-out.txt','a')
                output.write(val)
                output.write('\n')
                output.close()

            if 'pos' == str(val):
                output = open('posFeeds.txt','a')
                output.write(tweet)
                output.write('\n')
                output.close()
            elif 'neg' == str(val):
                output = open('negFeeds.txt','a')
                output.write(tweet)
                output.write('\n')
                output.close()
            
            return True

        except:
            return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["tax"])
