import config
from time import sleep
from random import randint, shuffle
from os import listdir

path = config.locale
hours = randint(3600, 7200)

def randomPic(path):
    listing = listdir(path)
    shuffle(listing)
    for i in listing:
        pic = path + i
    return pic
    
def tweetPicTrue(pic):
    photo = open(pic, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])

while True:
    print(randomPic(path))
    sleep(hours)
