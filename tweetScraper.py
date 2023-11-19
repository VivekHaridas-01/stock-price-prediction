from urllib import response
import tweepy
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
def scrape_tweet(word):
    tweets = tweepy.Cursor(api.search_tweets,
                            word,
                            until = "2022-05-01",
                            lang="en",
                                tweet_mode='extended').items(1188)
    db = pd.DataFrame(columns=['username',
                                    'following',
                                    'followers',
                                    'retweetcount',
                                    'text', 'date'])
    
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        date = tweet.user.created_at
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        retweetcount = tweet.retweet_count
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [username, following,
                        followers,
                        retweetcount, text, date]
        db.loc[len(db)] = ith_tweet

        i = i+1
    filename = f'scraped_tweets{word}.csv'
    # we will save our database as a CSV file.
    return db
    db.to_csv(filename)

if __name__ == '__main__':
    

    top_crypto = ['AAPL']

    auth = tweepy.OAuthHandler('4VgXD9imbmLUw5TaxsuyVaODH', 'eBQmGKl51BpL68diqwnvgffQIBVvbiPkvTPoNPeFuL86vE7UKr')
    
    # set access to user's access key and access secret 
    auth.set_access_token('1167786608021495809-7OZbF1QtybhkvoW7ze4h4WFXS5cPFG', '7T037wEETjgKgNbsiTspIabHQKkv0eNC30Ww2NzMJRFnf')
    api = tweepy.API(auth)

    for crypto in top_crypto:
        db=scrape_tweet(crypto)
        print (f'Done with {crypto}')
        print ("-------------------")