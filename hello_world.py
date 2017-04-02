

import tweepy

auth = tweepy.OAuthHandler('DXHicnqR5n4mGhJqQVz5hFDTF', 'vxMBxE3UfzuWhII6zYdKy2MEbHt6o28XBdzBvjSFNsNg80Omvh')
auth.set_access_token(	'3882823634-ki2NYIQyjoHPmmxbuNTrN72dNN1lnwAEgtY9KDO', 'Zp8rxqBlYRPbFRivBe7yO3Ut7jT2MNtxpZ603OJuV3EBC')


# to print output stream print post.text.encode('utf-8')

api = tweepy.API(auth)

api = tweepy.API(auth)

#to tweet
#api.update_status('Tweepy keep smiling!')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text).encode('utf-8')


for status in api.user_timeline('NiharikaRaut'):
	print(str(status.id)).encode('utf-8')
	#api.retweet(status.id)


