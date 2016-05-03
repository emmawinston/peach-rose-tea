import tweepy
import pycorpora
import random
import json
import os
import unidecode

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token_secret="foo"

access_token="foo"

consumer_key="foo"

consumer_secret="foo"


pitches = ['60', '62', '64', '66', '68']

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
          myfruit = []
          myfruit = random.choice(pycorpora.foods.fruits['fruits'])
          myfruitdecode = unidecode.unidecode(myfruit)
          print myfruitdecode + " (fruit)"

          pitch = (random.choice(pitches))

          singfruit = """osascript<<END
          say " """ + myfruitdecode + """ " using "junior" modulation 1 pitch """ + pitch + """ """

          os.system(singfruit)
          return True

        elif 'tea' in data:
          mytea = []
          mytea = random.choice(pycorpora.foods.tea['teas'])
          myteadecode = unidecode.unidecode(mytea)
          print myteadecode + " (tea)"

          pitch = (random.choice(pitches))

          singtea = """osascript<<END
          say " """ + myteadecode + """ " using "junior" modulation 1 pitch """ + pitch + """ """

          os.system(singtea)
          return True

        elif 'rose' in data:
          myflower = []
          myflower = random.choice(pycorpora.plants.flowers['flowers'])
          myflowerdecode = unidecode.unidecode(myflower)
          print myflowerdecode + " (flower)"

          pitch = (random.choice(pitches))
          
          singflower = """osascript<<END
          say " """ + myflowerdecode + """ " using "junior" modulation 1 pitch """ + pitch + """ """

          os.system(singflower)
          return True

    def on_error(self, status):
        print(status.text)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['fruit','tea','rose'])