import time
import codecs
import pandas as pd
import numpy as np
import requests
from PIL import Image
from io import BytesIO
import tweepy
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt

#Set up tweet API
consumer_key = "iZUDM7qHeP8KujdnK2viA4IKY"
consumer_secret = "GEzcP0jnzdoUyWSOHAtMX6NGo9TW5A3at8QCn2yQUL8MqodyN9"
access_key = "1430888243063517185-zmWhOaNNfjJ1BZ8GM84uvcH6jF2h3V"
access_secret = "vI8OI4HnXyHCYC1YyFfoLLrjJ2DKrBcaTtWVbGxbiJlu5"

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Creating an API object
api = tweepy.API(auth)


# Helper function for handling pagination in our search and handle rate limits
hashtag_tweets = tweepy.Cursor(api.search_tweets, q="#WM2022 OR #wmqatar", since="2022-06-29" ,tweet_mode='extended').items(10000)
# Define the term you will be using for searching tweets
query = '#WM2022 since:2022-04-02 until:2022-06-03'

tweet_data=[]
for tweet in hashtag_tweets:
    tweet_data.append(tweet)
    text = tweet._json["full_text"]
    print(text)
    #using different attributes
    print(tweet.id)
    print(tweet.favorite_count)
    print(tweet.retweet_count)
    print(tweet.created_at)

# Write tweet data to json file
with open('tweet_json.json', mode = 'w') as file:
    #_json property which contains JSON serializable response data. For example:
    json.dump([data._json for data in tweet_data], file)

#loading the data into a frame
basePath = os.path.dirname(os.path.abspath('tweet_json.json'))
tweet_api=pd.read_json(open('tweet_json.json',mode='r',encoding='utf-8'))