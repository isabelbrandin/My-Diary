import csv
import webbrowser

r_w = input("Do you want to read in your diary or write? [read / write] \n")

if r_w == "write":

    date = input("What date is it today? [dd-mm-yy] \n")
    rate = input("Can you rate your feeling on a scale 1-10 \n")
    feeling = input("How are you feeling today? \n")

    note = input("Can you tell me why? Did something happened? \n")
    sleep = input("How did you sleep last night? \n")
    sleeping =input("How much did you sleep? \n")
    con = input("Do you want to tell me something else? [yes/no] \n")

    if con == "yes":
        note2 = input("What did you had in mind? \n")
    elif con == "no":
        note2 = " "
        print("Okay, remember that i'm always here for you! I see you tomorrow.")

    Questions = [
        ["Can you rate your feeling on a scale 1-10 ", rate],
        ["How are you feeling today? ", feeling],
        ["Can you tell me why? Did something happened? ", note],
        ["How did you sleep last night?", sleep, sleeping],
        ["Do you want to tell me something else? ", con, note2],
    ]

    with open('diary.csv', 'a', newline='') as file:
        fieldnames = ['date', 'questions']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({'date': date, 'questions': Questions})

elif r_w == "read":

    day = input("Which day do you want to read? [dd-mm-yy] \n")
    
    with open('diary.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['date'], row['questions'])

