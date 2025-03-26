from filter import is_relevant

# Example tweets to test
example_tweets = [
    "Looking for a video editor for my YouTube channel",
    "Just had coffee with friends",
    "Need a graphic designer for my startup",
    "The weather is nice today",
    "Anyone know a good logo design service?",
    "Watching movies all day",
    "Hiring: Video Editor needed for short-term project",
    "Just finished my workout"
]

print("Testing keyword filtering with example tweets:\n")

for tweet in example_tweets:
    is_relevant_result = is_relevant(tweet)
    print(f"Tweet: {tweet}")
    print(f"Relevant: {'✅' if is_relevant_result else '❌'}")
    print("-" * 50) 