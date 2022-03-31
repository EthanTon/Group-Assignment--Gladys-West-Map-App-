"""
     Student: Ethan Ton
     Module: gladysUserInterface
     Description: This module does provides the user interface for the gladys
"""

import gladysUserLogin

# Login Functions


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

    startup_Input = raw_input()

    startup_Input = startup_Input.upper()

    return startup_Input


def login_Menu_Username():
    print("To exit login, type in break for username.")
    username_Input = raw_input("Please enter your username: ")

    return username_Input


def login_Menu_Password():
    password_Input = raw_input("Please enter your password: ")

    return password_Input

# User Stuff


# Main Menu
def main_Menu():
    """
    This function displays the main menu.
    """
    print("-------------------")
    print("Gladys West Map App")
    print("-------------------")




#Main Run
systemOn = True
doStartup = True
doMainSystem = True

username = ""

while systemOn:
     while doStartup:
          userInput = startup_Menu()
          if userInput == "L":
               username = gladysUserLogin.login()
               doStartup = False

          elif userInput == "C":
               gladysUserLogin.create_account()
          elif userInput == "E":
               doStartup = False
               systemOn = False
          else:
               print("Invalid input.")
     #while doMainSystem:
