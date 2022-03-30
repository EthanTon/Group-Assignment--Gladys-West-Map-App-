"""
Main Module
"""

import gladysUserInterface
import gladysUserLogin
import user

systemOn = True
doStartup = True
doMainSystem = True

username = ""

while systemOn:
    while doStartup:
        userInput = gladysUserInterface.startup_Menu()
        if userInput == "L":
            if gladysUserLogin.login() == 0:
                doStartup = False

        elif userInput == "C":
            gladysUserLogin.create_account()
        elif userInput == "E":
            doStartup = False
            systemOn = False
        else:
            print("Invalid input.")
    # while doMainSystem:
    
