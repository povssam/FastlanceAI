from outreach import alert_lead

def test_alert():
    print("Testing lead alert functionality...")
    
    # Example lead details
    lead_details = """
Client: John Smith
Project: Video Editing
Budget: $500-1000
Description: Looking for someone to edit a 10-minute YouTube video
Timeline: 1 week
    """.strip()
    
    try:
        print("Sending alert...")
        result = alert_lead("@yourusername", lead_details)  # Replace with your Telegram username
        print("Alert sent successfully!")
        print("Result:", result)
    except Exception as e:
        print(f"❌ Error sending alert: {str(e)}")
    finally:
        print("\nTest completed!")

if __name__ == "__main__":
    test_alert() 