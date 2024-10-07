# contacts.py

"""
Managing a list of friends. It allows adding, removing, and retrieving friends’ information 
(name, preferred greeting time, and contact information).
"""

import re  # Import regular expression module for email validation

class Contacts:
    def __init__(self):
        # Initialize an empty list to store contact information
        self.contacts = []

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        """
        Add a new contact to the contact list.

        Parameters:
        name (str): The name of the contact.
        email (str): The contact's email or phone number.
        preferred_time (str): The preferred time for greeting the contact.
        """
        # Normalize inputs
        name = name.strip().title()  # Normalize name
        email = email.strip().lower()  # Normalize email
        preferred_time = preferred_time.strip().upper()  # Normalize preferred time to uppercase

        # Validate the email format before adding the contact
        if not self._is_valid_email(email):
            print(f"Invalid email format: {email}")
            return

        # Validate the time format
        if not self._is_valid_time_format(preferred_time):
            print(f"Invalid time format: {preferred_time}. Please use 'HH:MM AM/PM'.")
            return

        # Check if the email already exists in the contact list to prevent duplicates
        if any(c['email'] == email for c in self.contacts):
            print(f"Contact with email {email} already exists. Cannot add '{name}'.")
            return

        # Create a contact dictionary with name, email, and preferred time
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        
        # Add the new contact to the contacts list
        self.contacts.append(contact)
        print(f"Contact added: {name} with email {email}")

    def remove_contact(self, name):
        """
        Remove a contact from the contact list by name.

        Parameters:
        name (str): The name of the contact to remove.
        """
        normalized_name = name.strip().title()  # Normalize the name for search by removing leading/trailing spaces and capitalizing each word
        matching_contacts = [c for c in self.contacts if c['name'] == normalized_name] # Find contacts that match the given name

        # If no matching contact is found, display a message and exit
        if not matching_contacts:
            print(f"Contact not found: {normalized_name}")
            return

        # If only one matching contact is found, remove it
        if len(matching_contacts) == 1:
            self.contacts.remove(matching_contacts[0])
            print(f"Removed contact: {normalized_name}")
        else:
            # If multiple contacts match the name, display them to the user
            print(f"Multiple contacts found for name '{normalized_name}':")
            self._display_contacts(matching_contacts)
            
            # Let the user choose which contact to remove
            choice = self._get_user_choice(len(matching_contacts), "remove")
            if choice is not None:
                # Remove the selected contact based on user input
                selected_contact = matching_contacts[choice - 1]
                self.contacts.remove(selected_contact)
                print(f"Removed contact with email: {selected_contact['email']}")

    def update_contact(self, name, new_email=None, new_preferred_time=None):
        """
        Update an existing contact's information.

        Parameters:
        name (str): The name of the contact to update.
        new_email (str): The new email of the contact (optional).
        new_preferred_time (str): The new preferred greeting time (optional).
        """ 
        normalized_name = name.strip().title()  # Normalize the name for search
        # Find contacts that match the given name
        matching_contacts = [c for c in self.contacts if c['name'] == normalized_name]

        # If no matching contact is found, display a message and exit
        if not matching_contacts:
            print(f"Contact not found: {normalized_name}")
            return

        # If multiple contacts match the name, let the user choose which one to update
        if len(matching_contacts) > 1:
            print(f"Multiple contacts found for name '{normalized_name}':")
            self._display_contacts(matching_contacts)
            contact_index = self._get_user_choice(len(matching_contacts), "update") - 1
            if contact_index is None:
                return # Exit if invalid choice
            contact = matching_contacts[contact_index]
        else:
            # If only one contact matches, proceed with the update
            contact = matching_contacts[0]

        # Update the email if a new one is provided or ask the user for a new email
        if new_email:
            new_email = new_email.strip().lower()  # Normalize the new email
            if self._is_valid_email(new_email):
                contact['email'] = new_email
            else:
                print(f"Invalid email format: {new_email}. Keeping the old one.")
        
        else:
            new_email = input("Enter the new email address (or press Enter to skip): ").strip().lower()
            if new_email and self._is_valid_email(new_email):
                contact['email'] = new_email
            if not self._is_valid_email(new_email):
                print("New email address is not valid. Keeping the old one.")

        # Update the preferred time if a new one is provided or ask the user for a new preferred time
        if new_preferred_time:
            new_preferred_time = new_preferred_time.strip().upper()  # Normalize to uppercase
            if self._is_valid_time_format(new_preferred_time):
                contact['preferred_time'] = new_preferred_time
            else:
                print(f"Invalid time format: {new_preferred_time}. Please use 'HH:MM AM/PM'.")
        else:
            new_preferred_time = input("Enter the new preferred time (or press Enter to skip): ").strip().upper()
            if new_preferred_time and self._is_valid_time_format(new_preferred_time):
                contact['preferred_time'] = new_preferred_time

        print(f"Updated contact: {contact['name']} to email: {contact['email']} and preferred time: {contact['preferred_time']}")

    def _get_user_choice(self, num_choices, action):
        """
        Prompt the user to select an option from a list of choices.

        Parameters:
        num_choices (int): The number of choices available.
        action (str): The action being performed (e.g., 'update', 'remove').

        Returns:
        int or None: The user's choice or None if invalid.
        """
        try:
            # Prompt the user to select a contact by number
            choice = int(input(f"Select which contact to {action} (1-{num_choices}): "))
            if 1 <= choice <= num_choices:
                return choice
            else:
                print("Invalid choice. No contact updated.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return None

    def _display_contacts(self, contacts):
        """
        Display a list of contacts with details (used for multi-contact selection).

        Parameters:
        contacts (list): A list of contact dictionaries to display.
        """
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")

    def _is_valid_email(self, email):
        """
        Validate the format of an email address.

        Parameters:
        email (str): The email address to validate.

        Returns:
        bool: True if the email is valid, False otherwise.
        """
        # Regular expression pattern for validating email addresses
        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        return re.match(email_regex, email) is not None

    def _is_valid_time_format(self, time_str):
        """
        Validate the preferred time format (e.g., 08:00 AM or 06:30 PM).

        Parameters:
        time_str (str): The time string to validate.

        Returns:
        bool: True if the time format is valid, False otherwise.
        """
        # Regular expression pattern for validating time strings in the format "HH:MM AM/PM"
        time_regex = r"^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$"
        return re.match(time_regex, time_str) is not None

    def get_contacts(self):
        """
        Retrieve all contacts.

        Returns:
        list: The list of all contacts.
        """
        return self.contacts

    def clear_contacts(self):
        """
        Clear all contacts from the list.
        """
        self.contacts = []
        print("Cleared all contacts.")