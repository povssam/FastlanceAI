from zapier_mcp import perform_action

# Supported messaging platforms
SUPPORTED_PLATFORMS = ["telegram", "twitter", "linkedin"]

# Message templates for different scenarios
TEMPLATES = {
    "greeting": "Hi {name}! 👋 I'm reaching out from Fastlance.",
    "project_interest": "I noticed you're looking for a {role}. I'd love to discuss how I can help with your project.",
    "follow_up": "Just checking in about the {project_type} project we discussed. Would love to hear your thoughts!"
}

def validate_platform(platform):
    """Validate if the platform is supported."""
    if platform.lower() not in SUPPORTED_PLATFORMS:
        raise ValueError(f"Unsupported platform. Please use one of: {', '.join(SUPPORTED_PLATFORMS)}")

def validate_message(message):
    """Validate if the message is not empty and within length limits."""
    if not message or not message.strip():
        raise ValueError("Message cannot be empty")
    if len(message) > 1000:  # Example limit
        raise ValueError("Message is too long (max 1000 characters)")

def send_message(platform, recipient, message):
    """
    Send a message to a recipient on a specific platform.
    
    Args:
        platform (str): The platform to send the message on (telegram, twitter, linkedin)
        recipient (str): The recipient's username or ID
        message (str): The message to send
        
    Returns:
        dict: The response from the Zapier action
    """
    # Validate inputs
    validate_platform(platform)
    validate_message(message)
    
    if not recipient or not recipient.strip():
        raise ValueError("Recipient cannot be empty")

    # Clean up recipient format
    recipient = recipient.strip()
    if platform == "telegram" and not recipient.startswith("@"):
        recipient = f"@{recipient}"

    return perform_action("send_message", {
        "platform": platform.lower(),
        "recipient": recipient,
        "message": message
    })

def send_template_message(platform, recipient, template_name, **kwargs):
    """
    Send a message using a predefined template.
    
    Args:
        platform (str): The platform to send the message on
        recipient (str): The recipient's username or ID
        template_name (str): The name of the template to use
        **kwargs: Variables to fill in the template
    """
    if template_name not in TEMPLATES:
        raise ValueError(f"Template not found. Available templates: {', '.join(TEMPLATES.keys())}")
    
    message = TEMPLATES[template_name].format(**kwargs)
    return send_message(platform, recipient, message)

def alert_lead(telegram_chat_id, lead_details):
    """
    Send a lead alert to a Telegram chat.
    
    Args:
        telegram_chat_id (str): The Telegram chat ID to send the alert to
        lead_details (str): Details about the lead
        
    Returns:
        dict: The response from the Zapier action
    """
    # Format the message nicely
    message = f"🚨 New Lead Alert!\n\n{lead_details}"
    
    # Send the message via Telegram
    return perform_action("send_message", {
        "platform": "telegram",
        "recipient": telegram_chat_id,
        "message": message
    }) 