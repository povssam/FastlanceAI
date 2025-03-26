from outreach import send_message, send_template_message

def test_outreach():
    print("Testing outreach functionality...\n")

    # Test 1: Direct message
    print("Test 1: Sending direct message")
    try:
        result = send_message(
            platform="telegram",
            recipient="@yourusername",  # Replace with your actual Telegram username
            message="Hello, testing Fastlance!"
        )
        print("✅ Direct message sent successfully!")
        print("Result:", result)
    except Exception as e:
        print(f"❌ Error sending direct message: {str(e)}")
    print("-" * 50)

    # Test 2: Template message - Greeting
    print("\nTest 2: Sending template message (greeting)")
    try:
        result = send_template_message(
            platform="telegram",
            recipient="@yourusername",  # Replace with your actual Telegram username
            template_name="greeting",
            name="John"  # Template variable
        )
        print("✅ Greeting template message sent successfully!")
        print("Result:", result)
    except Exception as e:
        print(f"❌ Error sending template message: {str(e)}")
    print("-" * 50)

    # Test 3: Template message - Project Interest
    print("\nTest 3: Sending template message (project interest)")
    try:
        result = send_template_message(
            platform="telegram",
            recipient="@yourusername",  # Replace with your actual Telegram username
            template_name="project_interest",
            role="video editor"  # Template variable
        )
        print("✅ Project interest template message sent successfully!")
        print("Result:", result)
    except Exception as e:
        print(f"❌ Error sending template message: {str(e)}")
    print("-" * 50)

if __name__ == "__main__":
    test_outreach() 