import tweepy

query = "#wm2022 OR #wmkatar -is:retweet"
client = tweepy.Client('')
counts = client.get_recent_tweets_count(query=query, granularity='day')

for i in counts.data:
    print(i["tweet_count"])