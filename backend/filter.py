KEYWORDS = ["video editor", "graphic designer", "logo design"]

def is_relevant(tweet_text):
    return any(keyword.lower() in tweet_text.lower() for keyword in KEYWORDS) 