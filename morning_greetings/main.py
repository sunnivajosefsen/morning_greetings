"""
Main script that integrates all the modules. The script performes the entire automation process: manage the contact list, 
create a personalized message for each contact, send the message, and record the operation in a log.
"""

import sys
import os

# Add the parent directory of the current script to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import morning_greetings.logger as log
import message_generator as msg_g
import message_sender as msg_s
from morning_greetings.contacts_manager import ContactsManager

def display_menu():
    """Display the menu options to the user."""
    print("\n--- Morning Greetings Menu ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. List Contacts")
    print("5. Clear Contacts")
    print("6. Send Message")
    print("7. Clear Log File(s)")
    print("8. Exit")
    print("-------------------------------")

def main():
    """Main program loop to manage the greeting process, handle user input, and perform actions."""
    
    # Initialize the ContactsManager to manage contact data
    manager = ContactsManager()
    
    while True:
        # Display the menu and get user's choice
        display_menu()
        choice = input("Choose an option (1-8): ")
        print("")

        if choice == '1':  # Add a new contact
            name = input("Enter the contact's name: ")
            email = input("Enter the contact's email: ")
            preferred_time = input("Enter the preferred time (e.g., 08:00 AM, leave blank for default): ")

            # If no preferred time is provided, use the default time
            if preferred_time.strip() == "":
                manager.add_contact(name, email)  # Call without passing preferred_time
            else:
                manager.add_contact(name, email, preferred_time)  # Call with preferred_time

        elif choice == '2':  # Remove a contact
            name = input("Enter the name of the contact to remove: ")
            manager.remove_contact(name)

        elif choice == '3':  # Update a contact's details
            manager.update_contact()

        elif choice == '4':  # List all contacts
            print("Listing all contacts:")
            manager.list_contacts()

        elif choice == '5':  # Clear all contacts from the contact list
            manager.clear_contacts()

        elif choice == '6':  # Send messages to all contacts
            contacts = manager.get_contacts()  # Retrieve all contacts
            
            if not contacts:  # If no contacts exist, notify the user and skip sending
                print("No contacts to send messages to.")
                continue

            # Iterate through all contacts and send a personalized message
            for contact in contacts:
                name = contact['name']
                email = contact['email']  # Ensure 'contact_info' matches your data structure
                message = msg_g.generate_message(name)  # Generate the "Good Morning" message
                preferred_time = contact['preferred_time']  # Get the preferred time

                try:
                    # Simulate sending the message at the preferred time
                    action = msg_s.calculate_time(contact, message, preferred_time)
                    log_file_name = f"{action}_messages_log.txt"  # Log based on whether the message was sent or planned

                    # Log the message (either in planned_messages_log.txt or sent_messages_log.txt)
                    log.log_message(contact, message, preferred_time=None, log_file=log_file_name)

                except ValueError as e:  # Handle any errors that occur during message sending
                    print(f"Error sending message to {name}: {e}")
        
        elif choice == '7':  # Clear the log files
            log_files = {
                "1": "planned_messages_log.txt",  # Option for planned log file
                "2": "sent_messages_log.txt",     # Option for sent log file
                "3": "both"                       # Option for both log files
            }

            print("Choose which log file(s) to clear:")
            print("1. Planned Messages Log")
            print("2. Sent Messages Log")
            print("3. Both")

            log_choice = input("\nEnter your choice (1, 2, or 3): ")

            if log_choice == '1':  # Clear only planned log
                try:
                    with open(log_files['1'], 'w') as file:
                        file.truncate()  # Empty the file
                    print(f"Cleared contents of {log_files['1']}.")
                except Exception as e:
                    print(f"Error clearing log file {log_files['1']}: {e}")

            elif log_choice == '2':  # Clear only sent log
                try:
                    with open(log_files['2'], 'w') as file:
                        file.truncate()  # Empty the file
                    print(f"Cleared contents of {log_files['2']}.")
                except Exception as e:
                    print(f"Error clearing log file {log_files['2']}: {e}")

            elif log_choice == '3':  # Clear both logs
                for log_file in [log_files['1'], log_files['2']]:
                    try:
                        with open(log_file, 'w') as file:
                            file.truncate()  # Empty the file
                        print(f"Cleared contents of {log_file}.")
                    except Exception as e:
                        print(f"Error clearing log file {log_file}: {e}")
            
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")


        elif choice == '8':  # Exit the program
            print("Exiting the program.")
            break

        else:  # Handle invalid menu option input
            print("Invalid option. Please try again.")

# Entry point of the program, calls the main function
if __name__ == "__main__":
    main()