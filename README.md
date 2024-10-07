# Morning Greatings Module
**Morning_Greatings_Module** is a Python package that automate the process of sending personlized "Good Morning" messages to a list of friends. It includes several modules, each handling a different aspect of the task, such as managing contacts, generating customized notifications, and simulating sending messages.

## Table of Contents
- [Morning Greatings Module](#morning-greatings-module)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
    - [Key Files:](#key-files)
  - [run the package locally](#run-the-package-locally)
  - [Run tests](#run-tests)

## Features
- Manage a list of friends (names, contact info, preferred greeting time)
- Generate personalized "Good Morning" messages
- Simulate sending messages
- Log messages with timestamps

## Installation
To get started, follow these steps:
1. **Clone the Repository** (or download the package):
   ```bash
   git clone 
   cd morning_greetings
   ```
2. **Create a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv greetingsenv
   source greetingsenv/bin/activate  # On Windows, use `gameenv\Scripts\activate`
   ```
1. **Install the Package**:
   ```bash
   pip install -e .
   ```
## Usage
Once installed, you can start the program by running the following command in your terminal:

```bash
morning_greetings
```
This will launch a menu where you can choose between the 8 available options:
1. **Add Contact**
2. **Remove Contact**
3. **Update Contact**
4. **List Contacts**
5. **Clear Contacts**
6. **Send Message**
7. **Clear Log File(s)**
8. **Exit**

## Project Structure
Here is a brief overview of the project's structure:
```
morning_greetings/
│
├── __init__.py                     # Empty
├── __main__.py                     # 
├── main.py                         # Entry point for the greetings menu
├── contact_manager.py              # Manage and load contacts
├── contacts.py                     # Manage list of friends
├── logger.py                       # Log sent messages
├── message_generator.py            # Generate personalized messages
├── message_sender.py               # Simulate sending messages
├── tests/
│   ├── __init__.py                 # Empty
│   ├── test_contacts.py            # Unit tests for contacts.py
│   ├── test_contacts_manager.py    # Unit tests for contact_manager.py
│   ├── test_logger.py              # Unit tests for logger.py
│   ├── test_message_generator.py   # Unit tests for message_generator.py
│   ├── test_message_sender.py      # Unit tests for message_sender.py
├── README.md                       # Project documentation (this file)
├── setup.py                        # Installation script
├── contacts.json                   # The contacts file will be saved here
├── planned_messages_log.txt        # Log for planned messages
└── sent_messages_log.txt           # Log for sent messages
```
### Key Files:
- **`main.py`**: Launches the greetings menu, letting users manage contacts.
- **`setup.py`**: Handles package installation, dependencies, and distribution setup.
- **`contacts.py`**: Manages friends list, including adding, removing, clearing, updating and list contact info.
- **`contact_manager`**: Manages the contacts (names and emails) in a structured way with json file, providing functions to load and save.
- **`message_generator.py`**: Generates personalized "Good Morning" messages for contacts.
- **`message_sender.py`**: Simulates sending messages to friends.
- **`logger.py`**: Logs sent and planned messages with timestamps in log files.

## run the package locally

Run the script manually:
python main.py

## Run tests

You can run all the tests by executing the following command from the package root directory:

python -m unittest discover tests


This will automatically discover and run all the test files (test_contacts.py, test_message_generator.py, test_message_sender.py, and test_logger.py).

These tests ensure that:

The generate_message function generates correct messages.
The send_message function works as expected and handles missing email addresses.
The log_message function writes the correct information to the log file.

