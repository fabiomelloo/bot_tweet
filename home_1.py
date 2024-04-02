import tweepy
consumer_key = "CmSWkBALEM21u6ngCbRIF0Wnp"
consumer_secret = "FCzKAsDjRxuimlEex9g6VOma2woORt0oCRR50xuOo68IuFXT4Z"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAMF0swEAAAAAIAO"
access_token = "887732196211142659-EY0SgnQeYZrFpbP68c7aRDzi1Oq6OOa"
access_token_secret = "CMJ0PT3upBzpWj6UIxVHLkT8pggHBQful3H421b8PXhWO"

# Autenticar
cleint = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret,access_token,access_token_secret)
api = tweepy.API(auth)
# tweetar 
cleint.create_tweet(text='OI MUNDAO')