from tweepy import OAuthHandler, API
import twitter_secrets
from os.path import join
from os import mkdir

def get_authorization():
    auth = OAuthHandler(twitter_secrets.consumer_key, twitter_secrets.consumer_secret, twitter_secrets.redirect_url)
    auth.set_access_token(twitter_secrets.access_token, twitter_secrets.access_token_secret)
    return auth

def get_api(working_auth):
    return API(working_auth)

def get_cache_path(id):
    return(join("cache", f'{str(id)}.cache'))

def create_cache_file(path):
    mkdir("cache")
    with open(path, 'w+'): 
        pass