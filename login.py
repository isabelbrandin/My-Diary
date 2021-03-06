import csv
import diary
import getpass

def create_user():
    print("\nCREATE YOUR ACCOUNT")
    new_username = input("Choose your username: ")
    new_password = getpass.getpass("Choose your password: ")
    with open('login.csv', 'a', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({fieldnames[0]: new_username, fieldnames[1]: new_password})
    login()

def user_exists(username, password):
    with open('login.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row['Username'] and password == row['Password']:
                return True
        return False


def login():
    print("\nLOGIN WITH YOUR USERNAME AND PASSWORD")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if user_exists(username, password):
        diary.run()
    else:
        choose = input("Do you want to try again or create a new user? \n[again / create] \n")
        if choose == "create":
            create_user()
        else:
            login()

login()

