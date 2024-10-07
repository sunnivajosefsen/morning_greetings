# message_sender.py

"""
Module to simulate sending the messages to each friend.
"""

import time # Importing time to simulate delays in sending messages
from datetime import datetime # Importing datetime to handle current and preferred times for sending
import logger as log # Importing the logger module to log the messages sent or planned


def calculate_time(contact, message, preferred_time=None):
    """
    Calculate the appropriate time to send a message based on the contact's preferred time.

    Parameters:
    contact (dict): A dictionary containing the contact's information.
    message (str): The message to be sent.
    preferred_time (str): The preferred time at which the message should be sent (optional).
    
    Returns:
    str: "planned" if the message is scheduled, "sent" if sent immediately.
    """
    if not contact['email']:
        raise ValueError("Email address is missing")  # Raise error if contact doesn't have an email
    if not message:
        raise ValueError("Message cannot be empty")  # Raise error if the message is empty
    
    # If a preferred time is provided, simulate waiting until that time to send the message
    if preferred_time:
        now = datetime.now()  # Get the current date and time
        preferred_time_dt = datetime.strptime(preferred_time, "%I:%M %p")  # Parse the preferred time
        # Set the preferred time to the current date
        preferred_time_dt = preferred_time_dt.replace(year=now.year, month=now.month, day=now.day)
        
        # Calculate the time difference between now and the preferred time
        delay_seconds = (preferred_time_dt - now).total_seconds()
        
        # If the preferred time is in the future, plan the message to be sent later
        if delay_seconds > 0:
            print(f"\nThe message will be sent to {contact['name']} with the email address {contact['email']} at the preferred time: {preferred_time}")
            
            # Simulate message scheduling by setting delay_seconds to 0 for this simulation
            delay_seconds = 0
            send_message(delay_seconds)  # Simulate message sending with the calculated delay

            return "planned"  # Indicate the message is planned
        
        # If the preferred time is in the past, send the message immediately and show a warning
        if delay_seconds < 0:
            print(f"\nPreferred time {preferred_time} has already passed. Sending message immediately to {contact['name']} with the email address {contact['email']}.")
            
            # Simulate sending the message immediately
            delay_seconds = 0
            send_message(delay_seconds)  # Simulate immediate message sending

            return "sent"  # Indicate the message has been sent
    
    if preferred_time == None: 
        print(f"Sending message to {contact['email']}: {message}")
        return "sent"

def send_message(delay_seconds):
    """
    Simulate sending a message after a delay.

    Parameters:
    delay_seconds (int): The number of seconds to wait before sending the message.
    """
    # Simulate sending the message by waiting for the specified delay time (0 in this case)
    time.sleep(delay_seconds)