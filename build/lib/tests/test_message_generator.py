# test_message_generator.py

import unittest
import os
import sys

# Dynamically add the project root directory to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from message_generator import generate_message  # Importing the generate_message function from the message_generator module

class TestMessageGenerator(unittest.TestCase):
    """Unit test class to test the message generation functionality."""
    
    def test_generate_message(self):
        """Test generating a personalized good morning message for a specific name."""
        name = "Alice"
        expected_message = "Good Morning, Alice! Have a great day!"  # Expected output when the name is Alice
        # Verify that the generated message matches the expected message
        self.assertEqual(generate_message(name), expected_message)  

    def test_generate_message_with_different_name(self):
        """Test generating a message for a different name."""
        name = "Bob"
        expected_message = "Good Morning, Bob! Have a great day!"  # Expected output when the name is Bob
        # Verify that the generated message matches the expected message for Bob
        self.assertEqual(generate_message(name), expected_message)  

    def test_generate_message_with_empty_name(self):
        """Test generating a message with an empty name."""
        name = ""
        expected_message = "Good Morning, ! Have a great day!"  # Expecting the message to still format correctly even if the name is empty
        # Verify that the generated message matches the expected message with an empty name
        self.assertEqual(generate_message(name), expected_message)  

    def test_generate_message_with_special_characters(self):
        """Test generating a message with a name that includes special characters."""
        name = "John @ Doe"
        expected_message = "Good Morning, John @ Doe! Have a great day!"  # Expected output with special characters in the name
        # Verify that the generated message matches the expected message when special characters are included
        self.assertEqual(generate_message(name), expected_message)  

if __name__ == "__main__":
    unittest.main()  # Run the tests when the script is executed directly
