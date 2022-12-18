import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("UZ3zWvswuMxLMF60juCk45IWw", "c0ZkeyMXcwC4jd6ZJ7hfvDEJzNUmNnBTJsf4DolyrTdBWHRtxS")
auth.set_access_token("1436240384888348677-aFliqdHSV7SivnOwuK4fOWj1vUNq9z", "bKtsQqVyeuyU6o94y5getLCB5vVbxURYpYPMWB6X7FSqI")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("123")