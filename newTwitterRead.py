from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = "q9vjzhnJZmEKfHpLwCMsGfJCE"
csecret = "gSX0omiVviHxyO5MV0LrKOzIV3O0zRbE56n0ucb4QpRKjIszYd"
atoken = "933415947276206080-sdyZ9CPqZfsqHN3ngYww0rUw2dnel0d"
asecret = "Y30c3tVcvd70IhgbvUyUExM5UHDfKg9QT4EGaz6i5OZHC"

class listener(StreamListener):

    def on_data(self,data):
        try:
            print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print tweet
            saveThis = str(time.time()) + '::' + tweet    
            saveFile = open('twitterNew.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'Failed on data' , str(e)
            time.sleep(5)

    def on_error(self,status):
        print status


auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["tax"])
