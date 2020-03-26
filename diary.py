import csv

def create_user():
    new_username = input("Choose your username: \n")
    new_password = input("Choose your password: \n")
    with open('login_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
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
        quiz.start()
    else:
        create_user()

login()

read_write = input("Do you want to read in your diary or write? [read / write] \n")
questions = open("questions.txt", "r").read().split(',')

if read_write == "write":
    date = input("What date is it today? [dd-mm-yy] \n")
    
    feeling = input(questions[0] + '\n')
    rate = input(questions[1] + '\n')
    note = input(questions[2] + '\n')
    sleep = input(questions[3] + '\n')
    naptime = input(questions[4] + '\n')
    con = input(questions[5] + '\n')

# Fler frågor?

    if con == "yes":
        note2 = input(questions[6] + '\n')
    elif con == "no":
        note2 = ' '
        print("Okay, remember that i'm always here for you! I see you tomorrow.")

    with open('diary.csv', 'a', newline='') as file:
        fieldnames = ['date', 'feeling', 'rate', 'note', 'sleep', 'naptime', 'con', 'note2']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        if note2 != ' ':
            writer.writerow({fieldnames[0]: date, fieldnames[1]: feeling, fieldnames[2]: rate, fieldnames[3]: note, fieldnames[4]: sleep, fieldnames[5]: naptime, fieldnames[6]: con, fieldnames[7]: note2})
        else:
            writer.writerow({fieldnames[0]: date, fieldnames[1]: feeling, fieldnames[2]: rate, fieldnames[3]: note, fieldnames[4]: sleep, fieldnames[5]: naptime, fieldnames[6]: con})

# Lista med videos, en relaterande video efter hur man mår skickas ut?

import webbrowser
import random

videos = ["https://www.youtube.com/watch?v=xVIbwE_eGK0" , "https://www.youtube.com/watch?v=5Cdv932eoU0" ,
 "https://www.youtube.com/watch?v=PI4JABNwB_U" , "https://www.youtube.com/watch?v=7Nn7NZI_LN4" , 
 "https://www.youtube.com/watch?v=gCAYhUkKUjU" , "https://www.youtube.com/watch?v=1-G6ufv3wG0" , 
 "https://www.youtube.com/watch?v=cjp3iq7fJsI" , "https://www.youtube.com/watch?v=LS_FPxmtz_U" , 
 "https://www.youtube.com/watch?v=4UaYMPfOMGI" , "https://www.youtube.com/watch?v=YJ73wMKovik" , 
 "https://www.youtube.com/watch?v=BT94ZwTGSQU" , "https://www.youtube.com/watch?v=H-zFRGP7MUQ" , 
 "https://www.youtube.com/watch?v=dRkQW-9XvBI" , "https://www.youtube.com/watch?v=PppkNH3bKV4" , 
 "https://youtu.be/26520P-sDmY" , "https://www.youtube.com/watch?v=JRnqdEZ8aoc" , 
 "https://www.youtube.com/watch?v=ur48jVNNlKk" , "https://www.youtube.com/watch?v=D-UmfqFjpl0" , 
 "https://www.youtube.com/watch?v=Ut-fJCc0zS4"
]

webbrowser.open_new(random.choice(videos))

music = ["https://www.youtube.com/watch?v=56WBK4ZK_cw" , "https://www.youtube.com/watch?v=DHwxF48LxPU" , 
"https://www.youtube.com/watch?v=Yim4--J44gk" , "https://www.youtube.com/watch?v=R_k31vxG26s" , 
"https://www.youtube.com/watch?v=LLUYAJO64DA" , "https://www.youtube.com/watch?v=bo59ICL2DsI" , 
"https://www.youtube.com/watch?v=rxf5ZGg9sQw" , "https://youtu.be/dy9nwe9_xzw" , 
"https://www.youtube.com/watch?v=KmVnOHjO6yU" , "https://www.youtube.com/watch?v=RfsAtKdATj0" , 
"https://www.youtube.com/watch?v=1OK1OqA-En4" , "https://www.youtube.com/watch?v=dhYOPzcsbGM" , 
"https://www.youtube.com/watch?v=60ItHLz5WEA" 

]

webbrowser.open_new(random.choice(music))

elif read_write == 'read':

    day = input('Which day do you want to read? [dd-mm-yy] \n')
    
    with open('diary.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if day == row['date']:
                answers = [row['feeling'],row['rate'],row['note'],row['sleep'],row['naptime'],row['con'],row['note2']]
                for i in range(len(questions)):
                    if answers[i] != '':
                        print('Q: ' + questions[i])
                        print('A: ' + answers[i].strip("'"))
                        print(' ')

