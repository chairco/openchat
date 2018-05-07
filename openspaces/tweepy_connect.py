import tweepy
from openspaces.secrets import openspaces, test_bot

def get_test_api():
    auth = tweepy.OAuthHandler(test_bot["CONSUMER_KEY"], test_bot["CONSUMER_SECRET"])
    auth.set_access_token(test_bot["ACCESS_TOKEN"], test_bot["ACCESS_TOKEN_SECRET"])
    return tweepy.API(auth)

def get_api():
    auth = tweepy.OAuthHandler(openspaces["CONSUMER_KEY"], openspaces["CONSUMER_SECRET"])
    auth.set_access_token(openspaces["ACCESS_TOKEN"], openspaces["ACCESS_TOKEN_SECRET"])
    return tweepy.API(auth)

def tweepy_send_tweet(tweet):
    api = get_api()
    status = api.update_status(status=tweet)
    return None

def tweepy_send_test_tweet(tweet):
    api = get_test_api()
    status = api.update_status(status=tweet)
    return None
