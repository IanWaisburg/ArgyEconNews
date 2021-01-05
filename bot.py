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

## Mention Retweet
#Last Mention Registration 
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
#Retweet if mentioned since last mention
def rts():
    print("Updating rts...",flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        api.retweet(mention.in_reply_to_status_id)
        if mention.user.screen_name != "Ian_Waisburg" or mention.user.screen_name != "SoySchrute": #Incentive System(might change later)
            api.update_status("Gracias @"+ mention.user.screen_name + " por compartir!")

## Auto Retweet Dolar Blue
#Last Dolar Blue Value Registration 
FILE_NAME_BLUE = 'last_blue_id.txt'

def retrieve_last_blue_id(file_name_blue):
    f_read = open(file_name_blue, 'r')
    last_blue_id = int(f_read.read().strip())
    f_read.close()
    return last_blue_id

def store_last_blue_id(last_blue_id, file_name_blue):
    f_write = open(file_name_blue, 'w')
    f_write.write(str(last_blue_id))
    f_write.close()
    return

# Dolar Blue Retweet
def blue():
    print("Updating Blue...",flush=True)
    last_blue_id = retrieve_last_blue_id(FILE_NAME_BLUE)
    bluetws = api.user_timeline(user_id = '1328362009', since_id = last_blue_id, tweet_mode = 'extended')
    for bluetw in reversed(bluetws):
        print(str(bluetw.id) + str(bluetw.created_at) + ' - ' + bluetw.full_text, flush=True)
        last_blue_id = bluetw.id
        store_last_blue_id(last_blue_id, FILE_NAME_BLUE)
        api.retweet(bluetw.id)
        


while True:
    rts()
    blue()
    time.sleep(45)