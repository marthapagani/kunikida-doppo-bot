import config
import secToHour
from random import randint
from os import listdir
from time import sleep

def randomPic(path):
    listing = listdir(config.locale)
    size = len(listing)
    if size > 0:

        while True:
            pos = (randint(0, size))
            kuni = listing[pos]
            while True:
                continue_input = input(f'Posso tweetar a foto {kuni}? ').upper()[0]
                if continue_input in 'SN':
                    break
                print('Opção inválida! ')
            if continue_input == 'S':
                break
        listing.pop(pos)

    else:
        print('Lista está vazia.')
        
    return path + kuni

def tweeting(kuni):
    photo = open(kuni, 'rb')
    tweet = config.twitter.upload_media(media=photo)
    config.twitter.update_status(status='', media_ids=[tweet['media_id']])

picture = randomPic(config.locale) # arquivo colocado em uma variável
hours = randint(900, 14000) # intervalo de tempo dos tweets
formated_hours = secToHour.timeConverter(hours)

while True:
    try:
        tweeting(picture)
        print(f'Tweetado com sucesso. Próximo tweet em {formated_hours}')
        sleep(hours)
    except Exception as e:
        print(f'Erro: {e}')
        break