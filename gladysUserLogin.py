
# Create a new user
def check_email(username):
    """
    Check if the email is valid
    """
    if "@" in username or "." in username:
        return True
    else:
        return False

def ask_for_email():
    """
    Ask for an email
    """
    email = input("Enter your email: ")
    # print (email)
    if check_email(email) == False:
        print("Invalid email")
        email = ask_for_email()
    return email

def ask_for_password():
    """
    Ask for a password
    """
    password = input("Enter your password: ")
    return password

def set_password():
    """
    Sets a password
    """
    password = input("Enter your password: ")
    if len(password) < 1:
        print("Password must be at least 1 character long")
        password = set_password()
    return password

def create_user():
    """
    Create a new user
    """
    email = ask_for_email()
    password = set_password()

    user_file = open("users.txt", "a")
    user_file.write(email + "," + password + "\n")



def login():
    


# create_user()  
    


