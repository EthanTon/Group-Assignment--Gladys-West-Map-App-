import gladysUserLogin



# class user():
#      """
#      User class
#      """

#      def __init__(self, email):
#           self.email = email





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

# main
def main():
     user = ""

     login_input = login_menu()
     if login_input == "L" :
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

print(main())
