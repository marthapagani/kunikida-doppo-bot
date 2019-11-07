import config
from random import sample
from os import listdir

def randomPic(path):
    choose = sample(range(len(listdir(path))), 1)
    pic = path + str(choose[0]) + '.png'
    return pic
    
def tweetPic(pic):
    photo = open(pic, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])

tweetPic(randomPic(config.locale))