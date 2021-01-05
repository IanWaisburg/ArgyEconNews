##Packages

import tweepy
import time

##Tweet Authentication
consumer_key = "LvbHgpqvUdGctfVQcefc4SAtF"
consumer_secret = "i86mMp0cOBluM5iENhpHVSINURkFO9giy9zYQ6sbzPIy7I3ljU"
access_token = "1345738596888834051-a8nKS8C7ZC3XRdn24mSsDWIvgDbLMg"
access_token_secret = "Gme8sCmVhzwt9ZCqttfkUrFVRl97pUeDAfWw1eRl9nNaz"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Upload PNG
api.update_with_media(filename = "dolar2_recortada.png", status = "Cotizaciones U$D al cierre: actualización diaria")
