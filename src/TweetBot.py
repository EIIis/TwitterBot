import tweepy

with open("account_info.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

accessKey = lines[0]
secretKey = lines[1]
consumerak = lines[2]
consumersk = lines[3]

auth = tweepy.OAuthHandler(consumerak, consumersk)
auth.set_access_token(accessKey, secretKey) # This is private for each user

api = tweepy.API(auth)


twitterUser = api.user_timeline(id = "ellis_alcantara") #user's twitter @ goes here
tweetid = 1320912308701454336
for tweet in twitterUser:
    if tweet.text[0:2] != "RT":
        api.update_status('@ellis_alcantara Test again :(', tweetid)

