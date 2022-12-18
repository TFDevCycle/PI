import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("UZ3zWvswuMxLMF60juCk45IWw", "c0ZkeyMXcwC4jd6ZJ7hfvDEJzNUmNnBTJsf4DolyrTdBWHRtxS")
auth.set_access_token("1436240384888348677-aFliqdHSV7SivnOwuK4fOWj1vUNq9z", "bKtsQqVyeuyU6o94y5getLCB5vVbxURYpYPMWB6X7FSqI")
api = tweepy.API(auth)

tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)