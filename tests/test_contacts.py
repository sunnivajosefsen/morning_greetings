# test_contacts.py

import unittest  # Importing the unittest module for creating test cases
import sys
import os

# Dynamically add the project root directory to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from morning_greetings.contacts import Contacts  # Importing the Contacts class for testing

class TestContacts(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Contacts instance for each test."""
        self.contacts = Contacts()  # Create a new instance of Contacts for testing

    def test_add_contact(self):
        """Test adding a new contact to the Contacts."""
        self.contacts.add_contact("Alice", "alice@example.com", "09:00 AM")  # Add a contact
        contacts = self.contacts.get_contacts()  # Retrieve the current list of contacts
        self.assertEqual(len(contacts), 1)  # Assert that there is one contact
        self.assertEqual(contacts[0]['name'], "Alice")  # Assert the contact's name is "Alice"

    def test_add_duplicate_contact(self):
        """Test adding a duplicate contact with the same name and email."""
        self.contacts.add_contact("Bob", "bob@example.com")  # Add a contact
        self.contacts.add_contact("Bob", "bob@example.com")  # Attempt to add duplicate
        contacts = self.contacts.get_contacts()  # Get current contacts
        self.assertEqual(len(contacts), 1)  # Assert that there is still only one contact
        self.assertEqual(contacts[0]['name'], "Bob")  # Assert the contact's name is "Bob"

    def test_add_duplicated_email(self):
        """Test adding contacts with different names but the same email."""
        # Add a contact and then try to add another contact with the same email
        self.contacts.add_contact("Bob", "bob@example.com")
        self.contacts.add_contact("Bob Junior", "bob@example.com")  # Duplicate email
        contacts = self.contacts.get_contacts()  # Retrieve current contacts
        self.assertEqual(len(contacts), 1)  # Assert that there is still only one contact
        self.assertEqual(contacts[0]['name'], "Bob")  # Assert the contact's name is "Bob"

    def test_add_duplicated_name(self):
        """Test adding contacts with the same name but different emails."""
        # Add two contacts with the same name but different email addresses
        self.contacts.add_contact("Bob", "bob@example.com")
        self.contacts.add_contact("Bob", "bobMarley@example.com")  # Same name, different email
        contacts = self.contacts.get_contacts()  # Get current contacts
        self.assertEqual(len(contacts), 2)  # Assert that there are now two contacts
        self.assertEqual(contacts[0]['name'], "Bob")  # Assert first contact is "Bob"
        self.assertEqual(contacts[0]['email'], "bob@example.com")  # Check first email
        self.assertEqual(contacts[1]['name'], "Bob")  # Assert second contact is also "Bob"
        self.assertEqual(contacts[1]['email'], "bobmarley@example.com")  # Check second email

    def test_remove_contact(self):
        """Test removing an existing contact."""
        self.contacts.add_contact("Bob", "bobMarley@example.com")  # Add a contact
        self.contacts.remove_contact("Bob")  # Remove the contact
        contacts = self.contacts.get_contacts()  # Retrieve current contacts
        self.assertEqual(len(contacts), 0)  # Assert that there are no contacts left

    def test_update_contact(self):
        """Test updating an existing contact's information."""
        self.contacts.add_contact("Alice", "alice@example.com", "09:00 AM")  # Add a contact
        # Update the contact's email and preferred time
        self.contacts.update_contact("Alice", new_email="alice_new@example.com", new_preferred_time="10:00 AM")
        updated_contact = self.contacts.get_contacts()[0]  # Get the updated contact
        self.assertEqual(updated_contact['email'], "alice_new@example.com")  # Assert the email is updated
        self.assertEqual(updated_contact['preferred_time'], "10:00 AM")  # Assert the preferred time is updated

    def test_remove_nonexistent_contact(self):
        """Test removing a contact that does not exist."""
        self.contacts.remove_contact("Nonexistent")  # Attempt to remove a non-existing contact
        self.assertEqual(len(self.contacts.get_contacts()), 0)  # Assert that there are still no contacts

    def test_update_nonexistent_contact(self):
        """Test updating a contact that does not exist."""
        self.contacts.update_contact("Nonexistent")  # Attempt to update a non-existing contact
        self.assertEqual(len(self.contacts.get_contacts()), 0)  # Assert that there are still no contacts

    def test_clear_contacts(self):
        """Test clearing all contacts from the manager."""
        self.contacts.add_contact("Alice", "alice@example.com", "09:00 AM")  # Add a contact
        self.contacts.add_contact("Bob", "bobMarley@example.com")  # Add another contact
        self.contacts.clear_contacts()  # Clear all contacts
        self.assertEqual(len(self.contacts.get_contacts()), 0)  # Assert that there are no contacts left

# Entry point for the test runner
if __name__ == "__main__":
    unittest.main()  # Run the tests
