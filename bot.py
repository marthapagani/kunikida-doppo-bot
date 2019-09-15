import config
from random import randint
from os import listdir

def randomPic(path):
    pic = randint(1, len(listdir(path)))
    pic = path + str(pic) + '.png'
    return pic
    
def tweetPic(pic):
    photo = open(pic, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])

tweetPic(randomPic(config.locale))