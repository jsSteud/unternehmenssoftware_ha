import tweepy
import csv
import pandas as pd

consumer_key = 'he9Uyd5xqSpQH0k9VL8qHYZmE'
consumer_secret = 'yZhQCJJslXtjUZYwbY7Lv3zCP37M9gDcKLv4GWAIwmcmObVlyB'
access_token = '1588247550901075971-KepTkrNtlPLBvBWEbvmhvfBQBMg1dr'
access_token_secret = 'hxApmBRaACJHISttpRTNtUQ5cZqU5kN7obyeyye4TFn6r'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('wm.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_30_day,
                            label= 'label',
                            query= '#wm2022 lang:de'
                          ).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])