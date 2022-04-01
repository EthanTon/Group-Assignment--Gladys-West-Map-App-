

# Create a new user
# Login Interface for Gladys


def ask_for_email():
    """
    Ask for an email
    """
    email = input("Enter your email: ")
    return email


def ask_for_password():
    """
    Ask for a password
    """
    password = input("Enter your password: ")
    return password


def check_email(username):
    """
    Check if the email is valid
    """
    if "@" in username and "." in username and not search_for_user(username):
        return True
    else:
        return False


def set_email():
    """
    Sets an email
    """
    email = ask_for_email()
    if check_email(email) == False:
        print("Invalid email")
        return set_email()
    return email


def set_password():
    """
    Sets a password
    """
    password = ask_for_password()
    if len(password) < 1:
        print("Password must be at least 1 character long")
        password = set_password()
    return password


def search_for_user(username):
    """
    Search for a user
    """
    user_file = open("users.txt", "r")
    for line in user_file:
        user_file_line = line.split(",")
        # print(user_file_line)
        if username == user_file_line[0]:
            return True
    return False


def create_user():
    """
    Create a new user
    """
    email = set_email()
    password = set_password()

    user_file = open("users.txt", "a")
    user_file.write(email + "," + password + "," + "\n")
    user_file.close()


def login():
    """
    Login
    """
    print("\n"+"Type \" break \" to go back to login menu")


    email = ask_for_email()
    password = ask_for_password()

    # print(email)
    
    if email == "break":
        return "back"
    elif search_for_user(email) == False:
        print("User not found! Make sure you have an account")
        return login()
    else:
        user_file = open("users.txt", "r")
        for line in user_file:
            # print(user_file)
            user_file = line.split(",")
            # print(user_file)
            if email == user_file[0] and password == user_file[1]:
                # print("Login successful")
                return email
        print("Wrong password")
        return login()


# create_user()

# print(login())
