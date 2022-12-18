# Importing all modules/packages/libraries
import tweepy
from textblob import TextBlob
import time
import colorama

# Initialization
auth = tweepy.OAuthHandler("UZ3zWvswuMxLMF60juCk45IWw", "c0ZkeyMXcwC4jd6ZJ7hfvDEJzNUmNnBTJsf4DolyrTdBWHRtxS")
auth.set_access_token("1436240384888348677-aFliqdHSV7SivnOwuK4fOWj1vUNq9z", "bKtsQqVyeuyU6o94y5getLCB5vVbxURYpYPMWB6X7FSqI")
api = tweepy.API(auth)

# Getting Bot ID
bot_id = int(api.me().id_str)

mention_id = 1

# Retweet Bot with Mentions
while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Tweet with @ found!")
        print("Tweet: " + colorama.Fore.BLUE + f"{mention.author.screen_name}" + colorama.Style.RESET_ALL  + colorama.Fore.BLUE + f" - {mention.text}" + colorama.Style.RESET_ALL + "\n")
        mention_id = mention.id
        mention_analysis = TextBlob(mention.text)
        mention_analysis_score = mention_analysis.sentiment.polarity
        print(f"Tweet has polarity score of  "+ colorama.Fore.GREEN + f"{mention_analysis_score}" + colorama.Style.RESET_ALL + "\n")
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if mention_analysis_score >= 0.0  and not mention.retweeted:
                try:
                    print("trying retweet...")
                    api.retweet(mention.id)
                    print(colorama.Fore.GREEN + "Tweet successfully retweeted!\n" + colorama.Style.RESET_ALL )
                except Exception as err:
                    print(err)
            else:
                print(colorama.Fore.RED + "Tweet will not be retweeted.\n" + colorama.Style.RESET_ALL )
    time.sleep(15)