import csv
import diary

def create_user():
    new_username = input("Choose your username: \n")
    new_password = input("Choose your password: \n")
    with open('login_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({fieldnames[0]: new_username, fieldnames[1]: new_password})
    login()

def user_exists(username, password):
    with open('login_data.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row['Username'] and password == row['Password']:
                return True
            else:
                return False

def login():
    username = input("Enter your username: \n")
    password = input("Enter your password: \n")
    if user_exists(username, password):
        diary.run()
    else:
        create_user()

login()