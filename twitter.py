import tweepy

# Twitter API credentials
consumer_key = "#####"
consumer_secret = "#####"
access_key = "#####"
access_secret = "#####"

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    all_tweets = []

    # Request newest tweets (max 200)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    # Save newest tweets in list
    all_tweets.extend(new_tweets)
    # id of oldest tweet
    oldest = all_tweets[-1].id - 1

    while len(new_tweets) > 0:
        print("Getting tweets before %s" % oldest)
        # All subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
        print("... %s tweets downloaded so far" % (len(all_tweets)))

    out_tweets = [tweet.text.encode("utf-8") for tweet in all_tweets]

    with open("%s_tweets.txt" % screen_name, "w+") as f:
        for item in out_tweets:
            if b"@" not in item and b"RT" not in item and b"http" not in item:
                f.write("%s\n" % item)

if __name__ == "__main__":
    get_all_tweets("pivokosa")
    # get_all_tweets("GordonRamsay")
    # get_all_tweets("Neguj_mo_srbski")