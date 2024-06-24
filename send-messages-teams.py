import requests

def send_message(webhook, message_text):
    """
    Sends a message to Microsoft Teams using the provided webhook URL.

    Parameters:
    webhook (str): The webhook URL for the Microsoft Teams channel.
    message_text (str): The text of the message to be sent.

    Returns:
    None: This function does not return any value.
    """
    message = {
        "text": message_text
    }
    response = requests.post(webhook, json=message)
    if response.status_code != 200:
        print('Failed to send message to Teams')
        print(response.text)
    else:
        print('Message sent to Teams')
    return None

if __name__ == "__main__":
    # Get your webhook from Teams channel (Settings -> Connectors -> Incoming Webhook)
    # Note: you need to have MS365 account to get the webhook (as of June 2024)
    TEAMS_WEBHOOK = ''
    
    MESSAGE_TEXT = 'hi'
    send_message(TEAMS_WEBHOOK, MESSAGE_TEXT)
    