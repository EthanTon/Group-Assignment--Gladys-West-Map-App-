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
    username = raw_input("Please enter your email address: ")

    while (username.find("@") == -1 or username.find(".") == -1):
        print("Invalid email address.")
        username = raw_input("Please enter your email address: ")

    while not check_avaiblity(username):
        username = raw_input(
            "Username already exists. Please enter a new username: ")

    password = raw_input("Please enter a password: ")
    add_user(username, password)
    print("Account created successfully.")


def login():
    """
    This function logs in the user.
    """
    login_Stop = "break"
    

    doLogin = True

    while doLogin:
        import gladysUserInterface
        username = gladysUserInterface.login_Menu_Username()
        password = gladysUserInterface.login_Menu_Password()

        if username == login_Stop:
            return "1"

        with open("users.txt", "r") as user_file:
            for line in user_file:
                user_file.read().strip().split(",")
                if username in line:
                    if password in line:
                        print("Login successful.")
                        # gladysUserInterface.user(username)
                        doLogin = False
                        return username
                    else:
                        print("Incorrect password.")
                else:
                    print("Your password or username is incorrect. Try Again.")
                    print("Make sure you have an account. If you don't, create one.")
