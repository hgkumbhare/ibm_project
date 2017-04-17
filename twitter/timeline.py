


CONSUMER_KEY = 'FHXFW5RsGUPdKWkLABm0I7wna'  
CONSUMER_SECRET = 'XzYuM6tse5C8MFaeMwmPDdc9Pkjm77XSwpLj5YVTtlUzKpYahl' 
ACCESS_KEY = '807685866088841216-3GrbWseOXRsjcXLgmlds3hnuGhl3xoE'  
ACCESS_SECRET = 'Rnig29YEJGuY8um5v4VbTDBImWw5xf2oNixGkLJBH5wYu' 


import tweepy
import json
import playVoice
import recordVoiceModule
import speechToTextModule
import readTweet

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def myTimeline():
    public_tweets = tweepy.Cursor(api.home_timeline).items(2)
    for tweet in public_tweets:
        x=tweet.text.encode('utf-8')
        print(x)
        #readTweet.textToSpeech(x)
        recepient=(tweet.user.screen_name)
        print(recepient)
        playVoice.playAudio('options.wav')
        recordVoiceModule.record('myOptionReply.wav')
        response=speechToTextModule.speechToText('myOptionReply.wav')

        
        if "reply" in response:
            recordVoiceModule.record('myOptionReply.wav')
            myReply=speechToTextModule.speechToText('myOptionReply.wav')
            x=tweet.id
            print(tweet.id)
            api.update_status('@'+recepient+ ' '+myReply,int(x))

        if "retweet" in response:
            api.retweet(tweet.id)

        #api.retweet(tweet.id)

        #print(tweet.id_str) 
        #api.update_status('@<username> My status update', 848463274031149056) * this is for reply *


    #for status in api.user_timeline('@JustForXposure'):
        #api.retweet(status.id)  * this is for retweet *

#for user in tweepy.Cursor(api.followers, screen_name="JustForXposure").items():
#    print (user.screen_name)
    # * this is for showing y followers*