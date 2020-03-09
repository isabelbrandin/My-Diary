import csv
import webbrowser

r_w = input("Do you want to read in your diary or write? [read / write] \n")
questions = open("questions.txt", "r").read().split(',')

if r_w == "write":
    date = input("What date is it today? [dd-mm-yy] \n")
    
    rate = input(questions[0])
    feeling = input(questions[1])
    note = input(questions[2])
    sleep = input(questions[3])
    naptime = input(questions[4])
    con = input(questions[5])
    if con == "yes":
        note2 = input(questions[6])
    elif con == "no":
        note2 = " "
        print("Okay, remember that i'm always here for you! I see you tomorrow.")

    with open('diary.csv', 'a', newline='') as file:
        fieldnames = ['date', 'rate', 'feeling', 'note', 'sleep', 'naptime', 'con', 'note2']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        if note2 != " ":
            writer.writerow({fieldnames[0]: date, fieldnames[1]: rate, fieldnames[2]: feeling, fieldnames[3]: note, fieldnames[4]: sleep, fieldnames[5]: naptime, fieldnames[6]: con, fieldnames[7]: note2})
        else:
            writer.writerow({fieldnames[0]: date, fieldnames[1]: rate, fieldnames[2]: feeling, fieldnames[3]: note, fieldnames[4]: sleep, fieldnames[5]: naptime, fieldnames[6]: con})

elif r_w == "read":

    day = input("Which day do you want to read? [dd-mm-yy] \n")
    
    with open('diary.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if day == row['date']:
                answers = [row['rate'],row['feeling'],row['note'],row['sleep'],row['naptime'],row['con'],row['note2']]
                for i in range(len(questions)):
                    if answers[i] != " ":
                        print('Q: ' + questions[i])
                        print('A: ' + answers[i].strip("'"))
                        print(' ')