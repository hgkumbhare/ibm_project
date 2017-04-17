import tweepy
import readTweet
import recordVoiceModule
import speechToTextModule
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet(myTweet):
  # Fill in the values noted in previous step here
  cfg ={ 
    "consumer_key"        : "FHXFW5RsGUPdKWkLABm0I7wna",
    "consumer_secret"     : "XzYuM6tse5C8MFaeMwmPDdc9Pkjm77XSwpLj5YVTtlUzKpYahl",
    "access_token"        : "807685866088841216-3GrbWseOXRsjcXLgmlds3hnuGhl3xoE",
    "access_token_secret" : "Rnig29YEJGuY8um5v4VbTDBImWw5xf2oNixGkLJBH5wYu" 
    }

  api = get_api(cfg)
  tweet = myTweet  
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

def twitter():
  recordVoiceModule.record('output.wav')
  myTweet=speechToTextModule.speechToText('output.wav')
  print(myTweet)
  ans=readTweet.textToSpeech(myTweet)
  if(ans==1):
   tweet(myTweet)