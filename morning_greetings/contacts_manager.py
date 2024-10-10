# contacts_manager.py

"""
Managing the contacts (names and emails) in a structured way

It provides functionality to add, update, remove, and list contacts using a 
Contacts class (presumed to be defined in the contacts.py file).
"""

import json
import os
from morning_greetings.contacts import Contacts


# Run this module as a single file?:
# from contacts import Contacts

class ContactsManager:
    def __init__(self, data_file="contacts.json"):
        """
        Initialize ContactsManager with the JSON file located in the morning_greetings module.

        Parameters:
        data_file (str): The name of the file where contact data is stored.
        """
        # Get the directory where this module is located
        module_dir = os.path.dirname(__file__)
        # Set the full path of the data file where contacts will be stored
        self.data_file = os.path.join(module_dir, data_file)
        # Create an instance of the Contacts class
        self.contacts = Contacts()

        # Load existing contacts from the data file during initialization
        self.load_data()

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        """
        Add a new contact to the contacts list.

        Parameters:
        name (str): The name of the contact.
        email (str): The email address of the contact.
        preferred_time (str): The preferred time for greeting the contact.
        """
    
        # Add the new contact to the list of contacts (if it doesn't already exist)
        self.contacts.add_contact(name, email, preferred_time)
        # Save the updated contacts list to the data file
        self.save_contacts()

    def remove_contact(self, name):
        """
        Remove a contact by name from the contacts list.

        Parameters:
        name (str): The name of the contact to be removed.
        """
        # Remove the contact from the list of contacts
        self.contacts.remove_contact(name)
        # Save the updated contacts list to the data file
        self.save_contacts()

    def update_contact(self, name=None, new_email=None, new_preferred_time=None):
        """
        Update contact information.

        Parameters:
        name (str): Name of the contact to be updated.
        new_email (str): New email of the contact.
        new_preferred_time (str): New preferred time for the contact.
        """
        # Get the current list of contacts
        contacts_list = self.contacts.get_contacts()  # Get contacts from the Contacts instance

        # If the contacts list is empty, print a message and exit
        if len(contacts_list) == 0:  # Check if contacts list is empty
            print("There are no contacts to update. The contact list is empty.")
            return 
        
        if name == None: 
            # Prompt the user to input the name of the contact to update
            name = input("Enter the name of the contact to update: ")
        
        # Update the contact information (email, preferred time)
        self.contacts.update_contact(name, new_email, new_preferred_time)
        # Save the updated contacts list to the data file
        self.save_contacts()

    def list_contacts(self):
        """
        Print the list of all contacts with their details.
        """
        # Retrieve all contacts
        contacts = self.contacts.get_contacts()
        # If no contacts are available, print a message and exit
        if not contacts:
            print("No contacts available.")
            return

        # Loop through each contact and print the details (name, email, preferred time)
        for contact in contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")

    def get_contacts(self):
        """
        Retrieve all contacts.

        Returns:
        list: List of all contacts.
        """
        # Return the list of contacts from the Contacts class instance
        return self.contacts.get_contacts()  # Get contacts from the Contacts instance
    
    def clear_contacts(self):
        """
        Clear all contacts from the list and save the changes.
        """
        # Clear all contacts from the Contacts class instance
        self.contacts.clear_contacts()
        # Save the empty contact list to the data file
        self.save_contacts()

    def save_contacts(self):
         """
         Save the current contacts to the data file in JSON format.
         """
         try:
            # Combine existing contacts into a dictionary where the key is the email
            all_contacts = {contact['email']: contact for contact in self.contacts.get_contacts()}

            # Save all contacts back to the file in JSON format
            with open(self.data_file, 'w') as file:
                json.dump(list(all_contacts.values()), file, indent=4)

            print(f"Contacts saved to {self.data_file}")

         except Exception as e:
            # Handle any error that occurs while saving the contacts
            print(f"Error saving contacts: {e}")
    
    def load_data(self):
        """
        Load existing contacts from the data file.
        """
        try:
            # Check if the data file exists
            if os.path.exists(self.data_file):
                # Check if the file is empty
                if os.stat(self.data_file).st_size == 0:
                    print("File found but empty. Initializing an empty list [].")
                    return []  # Return an empty list if the file is empty
                else:
                    # Load the data from the file
                    with open(self.data_file, 'r') as file:
                        existing_contacts = json.load(file)
                    
                    # Add the loaded contacts to the Contacts class instance
                    print("Load existing contacts: ")
                    for contact in existing_contacts:
                        self.contacts.add_contact(contact['name'], contact['email'], contact['preferred_time'])

            else:
                # If the file does not exist, print a message
                print("No existing contacts found.")

        except Exception as e:
            # Handle any error that occurs while loading the contacts
            print(f"Error loading contacts: {e}")