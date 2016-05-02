import tweepy
import pycorpora
import random



# print a random flower name

print random.choice(pycorpora.foods.fruits['fruits'])
print random.choice(pycorpora.plants.flowers['flowers'])
print random.choice(pycorpora.foods.tea['teas'])


OAUTH_SECRET    = "foo"

OAUTH_TOKEN     = "foo"

CONSUMER_KEY    = "foo"

CONSUMER_SECRET = "foo"


#################################### term searches ######################################################
#### PEACH #####

def track():

  # Prompt for login credentials and setup stream object

  TRACK_TERM = 'peach'

  api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

  f = api.request('statuses/filter', {'track': TRACK_TERM})

  for item in f:
    if 'text' in item:

      # print item['text'].split()
      splitTweet = item['text'].split()
      
      counts = []

      for t in splitTweet:
        try:
          counts.append(dictionary[t.lower()])
        except: 
          print ''

      item['counts'] = counts


      if 'retweeted_status' in item:

        item2 = item['retweeted_status']
        #print(item2['favorite_count'])
        #splitTweet = item2['favorite_count'].split()

        favorites = []

        favorites.append(item2['favorite_count'])
      
        sendOSC(item)