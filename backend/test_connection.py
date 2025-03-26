import requests
import time
import json

MCP_URL = "https://actions.zapier.com/mcp/sk-ak-AglzqUHf6Zw15TLNPS6KRcERIF/sse"

def test_connection():
    print("Testing connection to Zapier MCP endpoint...")
    print(f"URL: {MCP_URL}")
    start_time = time.time()
    
    headers = {
        'Accept': 'text/event-stream',
        'Cache-Control': 'no-cache'
    }
    
    query_params = {
        "action": "test",
        "test": "connection"
    }
    
    try:
        print("Sending GET request...")
        response = requests.get(MCP_URL, params=query_params, headers=headers, timeout=10)
        end_time = time.time()
        print(f"Connection successful! Response time: {end_time - start_time:.2f} seconds")
        print(f"Status code: {response.status_code}")
        print(f"Response headers: {response.headers}")
        
        # Handle SSE response
        events = response.text.strip().split('\n\n')
        print("\nProcessing events:")
        for i, event in enumerate(events, 1):
            print(f"\nEvent {i}:")
            print(event)
            if event.startswith('data: '):
                data = event.replace('data: ', '', 1)
                try:
                    json_data = json.loads(data)
                    print(f"Parsed JSON: {json_data}")
                except json.JSONDecodeError:
                    print("Not valid JSON data")
                    
    except requests.exceptions.Timeout:
        print("❌ Connection timed out after 10 seconds")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection failed: {str(e)}")
    finally:
        print("\nTest completed!")

if __name__ == "__main__":
    test_connection() 