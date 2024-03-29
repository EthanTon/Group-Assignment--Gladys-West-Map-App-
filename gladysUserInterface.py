"""
     Student: Ethan Ton
     Module: gladysUserInterface
     Description: This is the main system to display the menu and run the code.
"""

from cmath import sqrt
import random
import gladysUserLogin
import gladysSatellite
import gladysCompute

def runTests():
     gladysUserLogin.login()
     print(gladysSatellite.readSat(random.choice(["time","altitude","latitude","longitude"])))
     gladysSatellite.gpsValue(random.randint(0,99),random.randint(0,99), random.choice(["time","altitude","latitude","longitude"]))
     print("Test module complete")

def getX():
     try: 
          xpos = int(input("Enter X position: "))
     except ValueError:
          print("Invalid input")
          return getX()
     if xpos < 0 or xpos > 99:
          print("Invalid input")
          return getX()
     else:
          return xpos

def getY():
     try: 
          ypos = int(input("Enter Y position: "))
     except ValueError:
          print("Invalid input")
          return getY()
     if ypos < 0 or ypos > 99:
          print("Invalid input")
          return getY()
     else:
          return ypos
     

def login_menu():
     """
     Login menu
     """
     print("""
     Login Menu
     ---------------------
     [L] Login
     [C] Create an account
     [X] Exit
     ---------------------
     """)

     selection = input("Enter your selection: ")

     selection = selection.upper()

     return selection


def main_menu(user, user_xpos, user_ypos, destination_xpos, destination_ypos, distance):
     """
     Main menu
     """
     print("")
     print("Main Menu"+"\n"+"---------------------")
     print("User: " + user + "\n")

     print("Current position: " + str(user_xpos) + "," + str(user_ypos))
     print("Destination: " + str(destination_xpos) + "," + str(destination_ypos))
     print("Distance: " + str(distance))

     print("""
---------------------
[C] Set current position
[D] Set destination position
[M] Set distance - Map
[T] Run test module
[Q] Quit
---------------------
     """)

     selection = input("Enter your selection: ")

     selection = selection.upper()

     return selection

# main: Runs the entire program


def main():
     user = ""

     user_xpos = 0
     user_ypos = 0

     destination_xpos = 0
     destination_ypos = 0


     # login
     
     login_input = login_menu()
     if login_input == "L":
          email = gladysUserLogin.login()

          # print(email)

          if email == "back" or email == None:
               return main()
          else:
               print("Login successful")
               user = email

     elif login_input == "C":
          gladysUserLogin.create_user()
          print("Account created")
          return main()
     elif login_input == "X":
          print("Exiting...")
          return "Exit"
     else:
          print("Invalid input")
          return main()
     

     runMenu = True

     while runMenu == True:

          distance = gladysCompute.gpsDistance(user_xpos, user_ypos, destination_xpos, destination_ypos)

          menu_selection = main_menu(user, user_xpos, user_ypos, destination_xpos, destination_ypos, distance)

          # print(menu_selection)

          if menu_selection == "C":
               # Run set current position
               user_xpos = getX()
               user_ypos = getY()
          elif menu_selection == "D":
               # Run destination
               destination_xpos = getX()
               destination_ypos = getY()
          elif menu_selection == "M":
               # Run map
               print("---------------------")
               print("distance = " + str(distance))
               print("---------------------")
          elif menu_selection == "T":
               # Run test module
               runTests()
          elif menu_selection == "Q":
               print("Exiting...")
               runMenu = False
               return "Exit"
          else:
               print("Invalid input")


print(main())
