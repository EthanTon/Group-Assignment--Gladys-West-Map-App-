"""
     Student: Ethan Ton
     Module: gladysUserInterface
     Description: This module does provides provides login and logout functionality.
"""


def add_user(username, password):
    """
    This function adds a new user to user.txt.
    """
    with open("users.txt", "w") as user_file:
        user_file.write(username + "," + password + "\n")

def get_active_user():
    """
    This function returns the active user.
    """
    with open("users.txt", "r") as user_file:
        for line in user_file:
            username, password = line.split(",")
            return username

def check_avaiblity(username):
    """
    This function checks if the username is available.
    """
    with open("users.txt", "r") as user_file:
        for line in user_file:
            if username in line:
                return False
    return True

def create_account():
    """
    This function creates a new account for the user.
    """
    username = raw_input("Please enter a username: ")
    
    while not check_avaiblity(username):
        username = raw_input("Username already exists. Please enter a new username: ")

    password = raw_input("Please enter a password: ")
    add_user(username, password)
    print("Account created successfully.")