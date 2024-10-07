import unittest
import os
import sys
from datetime import datetime, timedelta

# Dynamically add the project root directory to sys.path for imports.
# This ensures that the message_sender module can be imported even when
# the test file is in a separate directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the calculate_time function from the message_sender module.
from message_sender import calculate_time

class TestMessageSender(unittest.TestCase):

    def test_calculate_time_sends_immediately(self):
        """Test if the message is sent immediately when no preferred time is provided."""
        # Set up a contact dictionary with a valid email.
        contact = {'name': 'Alice', 'email': 'alice@example.com'}
        # The message to be sent.
        message = "Good Morning!"
        
        # Call the function without specifying a preferred time, so the message should be sent immediately.
        result = calculate_time(contact, message)
        
        # Assert that the result is "sent", indicating the message was sent immediately.
        self.assertEqual(result, "sent")

    def test_calculate_time_with_future_preferred_time(self):
        """Test if the message is planned to be sent at a future preferred time."""
        # Set up a contact dictionary with a valid email.
        contact = {'name': 'Bob', 'email': 'bob@example.com'}
        # The message to be sent.
        message = "Good Morning!"
        # Specify a preferred time 1 hour from now.
        future_time = (datetime.now() + timedelta(hours=1)).strftime("%I:%M %p")
        
        # Call the function with the future preferred time, expecting it to be scheduled.
        result = calculate_time(contact, message, preferred_time=future_time)
        
        # Assert that the result is "planned", indicating the message is scheduled for the future.
        self.assertEqual(result, "planned")
        
    def test_calculate_time_with_past_preferred_time(self):
        """Test if the message is sent immediately when the preferred time has passed."""
        # Set up a contact dictionary with a valid email.
        contact = {'name': 'Charlie', 'email': 'charlie@example.com'}
        # The message to be sent.
        message = "Good Morning!"
        # Specify a preferred time 1 hour ago.
        past_time = (datetime.now() - timedelta(hours=1)).strftime("%I:%M %p")
        
        # Call the function with the past preferred time, expecting the message to be sent immediately.
        result = calculate_time(contact, message, preferred_time=past_time)
        
        # Assert that the result is "sent", indicating the message was sent immediately since the preferred time has passed.
        self.assertEqual(result, "sent")

    def test_calculate_time_missing_email(self):
        """Test that a ValueError is raised if the email is missing."""
        # Set up a contact dictionary with a missing email.
        contact = {'name': 'Alice', 'email': ''}
        # The message to be sent.
        message = "Good Morning!"
        
        # Use assertRaises to check that a ValueError is raised when the email is missing.
        with self.assertRaises(ValueError) as context:
            calculate_time(contact, message)
        
        # Assert that the raised error message matches the expected error.
        self.assertEqual(str(context.exception), "Email address is missing")

    def test_calculate_time_empty_message(self):
        """Test that a ValueError is raised if the message is empty."""
        # Set up a contact dictionary with a valid email.
        contact = {'name': 'Alice', 'email': 'alice@example.com'}
        # Provide an empty message.
        message = ""
        
        # Use assertRaises to check that a ValueError is raised when the message is empty.
        with self.assertRaises(ValueError) as context:
            calculate_time(contact, message)
        
        # Assert that the raised error message matches the expected error.
        self.assertEqual(str(context.exception), "Message cannot be empty")

if __name__ == "__main__":
    # Run the unit tests when this script is executed.
    unittest.main()