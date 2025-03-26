import requests
import json

TOKEN = "7540371289:AAENVwsDnn9IReOA4VOAx3Ko9a7ykR4bm4U"

def verify_token():
    print("Verifying bot token...")
    
    # Get bot info from Telegram API
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("ok"):
            bot_info = data.get("result", {})
            print("\n✅ Bot token is valid!")
            print(f"Bot username: @{bot_info.get('username')}")
            print(f"Bot name: {bot_info.get('first_name')}")
            print(f"Bot ID: {bot_info.get('id')}")
        else:
            print("\n❌ Bot token is invalid!")
            print(f"Error: {data.get('description')}")
            
    except Exception as e:
        print(f"\n❌ Error verifying token: {str(e)}")

if __name__ == "__main__":
    verify_token() 