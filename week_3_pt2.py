
from datetime import datetime
import time

#def calculateCalFromFat(fatGram):
#CalFromFat = int{}*9 

#def calculateCalFromCarb(carbGram): 
#CalFromCarb = int{}*4

#def calculateCalFromProtein (proteinGram):
#CalFromProtein = int{}*4

total_users = int(input("How many users in total? "))
users = {}
meals = ["breakfast", "brunch", "lunch", "dinner", "snacks"]

for _ in range(total_users) :
    name = input("Enter your name(s) here: ")
    users[name] = {}

    goal = float(input("Okay %s, how many calories are you looking foward to eat today " % (name)))
    if goal <= 1500 and goal >= 601:
        print("That is considered healthy, good option!")
    elif goal <= 600:
        print("Don't malnourish yourself!")
    elif goal >= 2000:
        print("That isn't really suitable but it's your life so do what you want. Ave. amt of calories that are equal to one pound is apromiximately 3500 calories.")
    users[name]["goal"] = goal
    users[name]["meals"] = []

    for meal in meals :
        if meal == "snacks" :
            question = input("Did you eat any snacks today? If yes, type 'yes' if no then type 'no'")
            if not(question == 'yes' or question == 'Yes') :
                continue
        cals = float(input("Enter %s calories: " % meal))
        users[name]["meals"].append(cals)


        userFat = float(input('Enter fat grams:'))
        userCarb = float(input('Enter carb grams:'))
        userProtein = float(input('Enter protein grams:'))
        users[name]["userFat"] = []
        users[name]["userCarb"] = []
        users[name]["userProtein"] = []

 
    users[name] = sum(users[name]["meals"])

print("Awesome! Let's see what your intake today was!")

print ("")
now = datetime.now()
print ("       %s/%s/%s     " % (now.month, now.day, now.year))
print ("  ------------------")
print ("Name             Cals")
print ("  ------------------")
for name in users :
    print ("{}             {}".format(name, users[name]))
print ("  ------------------")
print ("Amt of Fat Grams: {}")
print ("Amt of Protein Grams:{}")
print ("Amt of Carb Grams: {}")
