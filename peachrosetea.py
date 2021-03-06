import tweepy
import pycorpora
import random
import json
import os
import unidecode
import time

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token_secret="foo"

access_token="foo"

consumer_key="foo"

consumer_secret="foo"

pitches = ['57', '60', '62', '65', '69', '72', '74']
times = [1, 2, 3, 4, 5]

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
          time.sleep(random.choice(times))
          return True

        elif 'tea' in data:
          mytea = []
          mytea = random.choice(pycorpora.foods.tea['teas'])
          myteadecode = unidecode.unidecode(mytea)
          pitch = (random.choice(pitches))

          print myteadecode + " (tea)"

          singtea = """osascript<<END
          say " """ + myteadecode + """ " using "junior" modulation 1 pitch """ + pitch + """ """

          os.system(singtea)
          time.sleep(random.choice(times))
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
          time.sleep(random.choice(times))
          return True

    def on_error(self, status):
        print(status.text)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['fruit','tea','rose'])