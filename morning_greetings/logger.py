# logger.py

"""
Module to log the messages that were "sent" or are planned to be "sent" to each friend.
"""

import datetime  # Importing datetime to add timestamps to the log entries

# The log_message method logs details of a message that was sent, including the contact's name,
# email, the message content, and the time when it was sent. It also allows logging messages
# at the preferred time if specified by the user.

def log_message(contact, message, preferred_time=None, log_file: str = "message_log.txt"):
    """
    Log a message indicating it was sent to a contact.

    Parameters:
    contact (dict): A dictionary containing the contact's information (name, email, etc.).
    message (str): The message that was sent to the contact.
    preferred_time (str): The preferred time when the message was sent (optional).
    log_file (str): The name of the log file to write the log entry to (default is "message_log.txt").
    """
    
    # Create a log entry string that includes the current timestamp, contact's name, email, 
    # the preferred time (if provided), and the message content.
    log_entry = (f"{datetime.datetime.now()} - Sent to {contact['name']} "
                 f"({contact['email']}) at {preferred_time if preferred_time else 'N/A'}: {message}\n"
                 )
    
    # Error handling: Attempt to open the log file and append the log entry. 
    # If an error occurs, print an error message.
    try:
        with open(log_file, "a") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Error logging message: {e}")  # Print error details if logging fails
