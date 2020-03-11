import csv
import webbrowser

# Inloggning?

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
