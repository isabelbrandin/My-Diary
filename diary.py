
feeling = input("How are you feeling today? \ngood, happy, sad, mad, fine, stressed, idk \n")
rate = input("Can you rate your feeling on a scale 1-10 \n")

if feeling == "happy" or "good" or "fine":
    note = input("That is nice to hear! Tell me more :) \n")
else:
    note2 = input("Can you tell me why? Did something happened? \n")

con = input("Do you want to tell me something else? [yes/no]")

if con == "yes":
    input("What did you had in mind?")
elif con == "no":
    print("Okay, remember that i'm always here your you! I see you tomorrow.")

# input("What is taking up most of my headspace? ")

# input("When did you last eat a whole meal? ")

# input("How much sleep did you get last night? ")