from twitter import fetch_replies

# Test with a known Twitter user ID (e.g., @jack's ID: 12)
test_user_id = "12"

try:
    print(f"Fetching replies for user ID: {test_user_id}")
    replies = fetch_replies(test_user_id)
    
    if replies:
        print(f"\nFound {len(replies)} replies:")
        for reply in replies:
            print(f"\nTweet ID: {reply.id}")
            print(f"Text: {reply.text}")
            print(f"Referenced Tweet ID: {reply.referenced_tweets[0].id}")
    else:
        print("No replies found for this user.")
        
except Exception as e:
    print(f"An error occurred: {str(e)}") 