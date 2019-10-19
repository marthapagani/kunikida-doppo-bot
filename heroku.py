from time import sleep
from twython import Twython

# API KEYS
APP_KEY = 'QvZ9OvpEA6yxgd8ediZCvUhiw'
APP_SECRET = 'E6urktic3goTW5rajerHhxCT7DrEnwbpGFIaET0zkIcLdbJUJt'
# ACCESS TOKEN
OAUTH_TOKEN = '1148803609422905344-R4ICLi9gpWVimg40oAzVuJjSc28mXC'
OAUTH_TOKEN_SECRET = 'Z8GzqSFit01M67jmiw2dLRVQoR2iAf6VLVo1pfeH2lxf7'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

listing = [
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/1.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/2.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/3.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/4.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/5.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/6.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/7.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/8.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/9.png',
    'https://raw.githubusercontent.com/cibertetica/kunikida-doppo-bot/master/images/10.png',
]

for i in listing:
    '''photo = open(i, 'rb')
    tweet = twitter.upload_media(media=photo)
    twitter.update_status(status='', media_ids=[tweet['media_id']])
    sleep(18000)'''
    print(i)