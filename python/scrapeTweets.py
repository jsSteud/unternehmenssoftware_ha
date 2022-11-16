import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('../csv/november.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Timestamp", "Tweet", "Hashtags", "Tweet_ID"])
counter = 0

for tweet in tweepy.Cursor(api.search_30_day,
                            #label must be set account specific!
                            label= '',
                            query= '#wm2022 OR #wmkatar lang:de',
                            fromDate = "202211150000",
                            toDate = "202211160000"
                          ).items():

    print (counter)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.entities.get('hashtags'),tweet.id])
    counter += 1

