# import tweepy
import helpers

api = helpers.get_api(helpers.get_authorization())
my_id = (api.me()._json["id"])
cache_path = helpers.get_cache_path(my_id)
try:
    helpers.create_cache_file(cache_path)
except FileExistsError:
    print("Error: Can not create cache")

# public_tweets = api.home_timeline()
# following = api.friends()

# for follow in tweepy.Cursor(api.friends).items():
#     print(follow._json['screen_name'])