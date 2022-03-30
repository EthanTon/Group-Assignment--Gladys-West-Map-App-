"""
     Student: Ethan Ton
     Module: gladysUserInterface
     Description: This module does provides the user interface for the gladys
"""

import gladysUserLogin

def startup_Menu():
     """
     This function displays the login menu.
     """
     print("Select an option:")
     print("-------------------")
     print("[L] Login")
     print("[C] Create Account")
     print("[E] Exit")
     print("-------------------")

     startup_Input = raw_input("")

     startup_Input = startup_Input.upper()

     return startup_Input

def login_Menu_Username():
     print("To exit login, type in break for username.")
     username_Input = raw_input("Please enter your username: ")
     
     return username_Input

def login_Menu_Password():
     password_Input = raw_input("Please enter your password: ")
     
     return password_Input