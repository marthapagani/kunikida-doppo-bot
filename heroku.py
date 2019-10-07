from time import sleep
from os import listdir, environ
from twython import Twython

locale = 'images/'

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

for i in listdir(locale):
    pic = locale + i
    photo = open(pic, 'rb')
    tweet = twitter.upload_media(media=photo)
    twitter.update_status(status='', media_ids=[tweet['media_id']])
    sleep(18000)