# test_logger.py

import unittest
import os
import sys

# Dynamically add the project root directory to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logger import log_message  # Importing the log_message function to test


class TestLogger(unittest.TestCase):
    def setUp(self):
        """Set up a temporary log file for testing."""
        self.log_file = "test_message_log.txt"  # Temporary log file for tests
        # Remove the log file if it already exists
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        """Clean up the temporary log file after testing."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)  # Remove the log file after the test

    def test_log_message(self):
        """Test logging a message to the log file."""
        contact = {'name': 'Alice', 'email': 'alice@example.com'}
        message = "Hello, Alice!"
        
        log_message(contact, message, log_file=self.log_file)  # Log a message
        
        # Verify that the log file was created and contains the expected entry
        self.assertTrue(os.path.exists(self.log_file))  # Check if the log file exists
        
        with open(self.log_file, 'r') as file:
            log_content = file.read()  # Read the content of the log file
            
            # Check that the log content includes the contact's name and message
            self.assertIn('Sent to Alice', log_content)  # Verify the name is logged
            self.assertIn('alice@example.com', log_content)  # Verify the email is logged
            self.assertIn(message, log_content)  # Verify the message content is logged
            
            # Check if the timestamp is present
            self.assertIn('-', log_content.splitlines()[0])  # Verify timestamp is logged

    def test_log_message_with_preferred_time(self):
        """Test logging a message with a preferred time."""
        contact = {'name': 'Bob', 'email': 'bob@example.com'}
        message = "Hi Bob!"
        preferred_time = "10:00 AM"
        
        log_message(contact, message, preferred_time=preferred_time, log_file=self.log_file)  # Log a message
        
        # Verify that the log file was created and contains the expected entry
        self.assertTrue(os.path.exists(self.log_file))  # Check if the log file exists
        
        with open(self.log_file, 'r') as file:
            log_content = file.read()  # Read the content of the log file
            
            # Check that the log content includes the contact's name, message, and preferred time
            self.assertIn('Sent to Bob', log_content)  # Verify the name is logged
            self.assertIn('bob@example.com', log_content)  # Verify the email is logged
            self.assertIn(message, log_content)  # Verify the message content is logged
            self.assertIn(preferred_time, log_content)  # Verify the preferred time is logged

if __name__ == "__main__":
    unittest.main()  # Run the tests