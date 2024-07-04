# User Checker

User Checker is a Python-based tool designed to fetch and display detailed information about a specified Discord user.

## Requirements
- Python 3.x
- `requests` library (Install it using `pip install requests`)
- `colorama` library (Install it using `pip install colorama`)

To get started, ensure you have the necessary dependencies by running `pip install -r requirements.txt` in your terminal.

## Usage
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Open a terminal or command prompt in the cloned directory.
4. Run the following command to start the tool:

    ```bash
    python main.py
    ```
    
5. Input the target Discord user's ID when prompted.
6. The tool will display the user's information including their ID, username, global name, discriminator, creation date, badges, avatar link, banner link, and banner color.

## Code Explanation

The main script performs the following actions:

1. **Imports Required Libraries**:
    - `os`: For clearing the terminal screen.
    - `requests`: For making HTTP requests to fetch user data from the API.
    - `colorama`: For adding colors to the terminal output.
    - `datetime`: For parsing and manipulating dates and times.

2. **Determine Clear Command**:
    - Sets the appropriate command to clear the terminal screen based on the operating system.

3. **Main Loop**:
    - Continuously prompts the user to enter a Discord user ID until the user types 'exit'.

4. **Fetch User Data**:
    - Makes a GET request to the API endpoint `https://discordlookup.mesalytic.moe/v1/user/{user_id}` with the entered user ID.
    - If the request is successful (status code 200), it parses and displays the user's information.
    - Handles potential errors such as invalid user ID or request failures.

5. **Display User Information**:
    - Clears the terminal screen and prints the user's details including ID, username, global name, discriminator, creation date, badges, avatar link, banner link, and banner color.

## Usage Caution
- This tool is intended for educational or testing purposes only.
- Usage for malicious intent is strongly discouraged and unethical.
- Use responsibly and adhere to ethical standards while interacting with Discord users.

Remember, use this tool responsibly and ethically. Any misuse or violation of Discord's terms of service is the responsibility of the user.
