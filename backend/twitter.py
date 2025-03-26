import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAAya0AEAAAAAdo8RV8xeK6HD7acPO1fcmluN2zg%3D0DgDhyWFlkeHlsAModnBtvpmYekVk5ia5vGBlIrtRpb6SFt4LM')

def fetch_replies(user_id):
    tweets = client.get_users_tweets(id=user_id, tweet_fields=['referenced_tweets'], max_results=20)
    replies = [t for t in tweets.data if t.referenced_tweets]
    return replies 