"""
     Student: Ethan Ton
     Module: gladysUserInterface
     Description: This module does provides provides login and logout functionality.
"""

def add_user(username, password):
    """
    This function adds a new user to user.txt.
    """
    with open("user.txt", "a") as user_file:
        user_file.write(username + "," + password + "\n")

def create_account():
    """
    This function creates a new account for the user.
    """
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    add_user(username, password)