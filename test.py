import config
from time import sleep
from random import randint, shuffle
from os import listdir

hours = randint(7200, 14400) # tempo aleatório
config.locale # local onde estão salvos os arquivos
listing = listdir(config.locale)

def randomPic(path):
    size = len(listing)
    if size > 0:
        randpic = randint(0, size)
        archive = listing[randpic]
        listing.pop(randpic)
    else:
        print('I already tweeted everything...')
    pic = path + archive
    return pic

picture = randomPic(config.locale)

def tweeting(picture):
    photo = open(picture, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])
    sleep(hours)

def loop(picture):
    while True:
        try:
            tweeting(picture)
        except Exception as error:
            print(f'We have an actual error here... {error}')
            break

loop(picture)