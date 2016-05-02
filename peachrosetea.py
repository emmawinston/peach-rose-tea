import tweepy
import pycorpora
import random
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token_secret="foo"

access_token="foo"

consumer_key="foo"

consumer_secret="foo"


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        if 'fruit' in data:
          print random.choice(pycorpora.foods.fruits['fruits']) + " (fruit)"
          return True
        elif 'tea' in data:
          print random.choice(pycorpora.foods.tea['teas']) + " (tea)"
          return True
        elif 'rose' in data:
          print random.choice(pycorpora.plants.flowers['flowers']) + " (flower)"
          return True

    def on_error(self, status):
        print(status.text)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['fruit','tea','rose'])