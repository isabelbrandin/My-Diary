import csv
import webbrowser

date = input("What date is it today? [dd-mm-yy] \n")
rate = input("Can you rate your feeling on a scale 1-10 \n")
feeling = input("How are you feeling today? \n")

note = input("Can you tell me why? Did something happened? \n")
sleep = input("How did you sleep last night?")
sleeping =input("How much did you sleep?")
con = input("Do you want to tell me something else? [yes/no] \n")

if con == "yes":
    note2 = input("What did you had in mind? \n")
elif con == "no":
    note2 = " "
    print("Okay, remember that i'm always here for you! I see you tomorrow.")

Questions = [
    [date],
    ["Can you rate your feeling on a scale 1-10 ", rate],
    ["How are you feeling today? ", feeling],
    ["Can you tell me why? Did something happened? ", note],
    ["How did you sleep last night?", sleep, sleeping],
    ["Do you want to tell me something else? ", con, note2],
    [" "]
]

with open('diary.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(Questions)
