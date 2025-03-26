import requests
import json
from requests.exceptions import Timeout, RequestException

MCP_URL = "https://actions.zapier.com/mcp/sk-ak-AglzqUHf6Zw15TLNPS6KRcERIF/sse"

def perform_action(action, params):
    try:
        # Prepare headers
        headers = {
            'Accept': 'text/event-stream',  # SSE endpoint expects this
            'Cache-Control': 'no-cache'
        }
        
        # Prepare query parameters
        query_params = {
            "action": action,
            **params  # Expand params into query parameters
        }
        
        print(f"Sending request to {MCP_URL}")
        print(f"Action: {action}")
        print(f"Params: {params}")
        
        # Send GET request
        response = requests.get(MCP_URL, params=query_params, headers=headers, timeout=10)
        response.raise_for_status()
        
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Raw response: {response.text}")
        
        # For SSE responses, we might get multiple events
        events = response.text.strip().split('\n\n')
        for event in events:
            if event.startswith('data: '):
                data = event.replace('data: ', '', 1)
                try:
                    return json.loads(data)
                except json.JSONDecodeError:
                    continue
        
        raise ValueError("No valid JSON data found in response")
        
    except Timeout:
        print("Request timed out after 10 seconds")
        raise
    except RequestException as e:
        print(f"Request error: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {str(e)}")
        print(f"Response content: {response.text}")
        raise 