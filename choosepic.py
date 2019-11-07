import config
from random import sample
from os import listdir
from time import sleep

def randomPic(path):
    while True:
        choose = sample(range(len(listdir(path))), 1)
        option = input(f'Tweetar foto {choose}? [S/N] ').upper()[0]
        if option not in 'SN':
            print('Opção inválida! ')
        if option in 'S':
            break
    pic = path + str(choose[0]) + '.png'
    return pic
    
def tweetPic(pic):
    photo = open(pic, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])
    sleep(2)

tweetPic(randomPic(config.locale))