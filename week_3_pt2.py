
from datetime import datetime
import time

def calculateCalFromFat(fatGram):
    CalFromFat = fatGram * 9 
    return CalFromFat

def calculateCalFromCarb(carbGram): 
    CalFromCarb = carbGram * 4
    return CalFromCarb

def calculateCalFromProtein (proteinGram):
    CalFromProtein = proteinGram * 4
    return CalFromProtein



total_users = int(input("How many users in total? "))
users = {}
meals = ["breakfast", "brunch", "lunch", "dinner", "snacks"]
fcp = ["Calories of Fat",  "Calories of Carbs", "Calories of Protein"]
for _ in range(total_users) :
    name = input("Enter your name(s) here: ")
    users[name] = {}

    goal = float(input("Okay %s, how many calories are you looking foward to eat today " % (name)))
    if goal <= 1500 and goal >= 501:
        print("That is very healthy and ideal")
    elif goal <= 500:
        print("Don't malnourish yourself!")
    elif goal >= 2000:
         print("That isn't really suitable but it's your life so do what you want. Ave. amt of calories that are equal to one pound is apromiximately 3500 calories.")
    users[name]["goal"] = goal
    users[name]["meals"] = []

    for meal in meals :
        if meal == "snacks" :
            question = input("Did you eat any snacks today? If yes, put in amt of calories of snack/ if not just put no ")
            if not(question == 'no' or question == 'No') :
                continue
        cals = float(input("Enter %s calories: " % meal))
        users[name]["meals"].append(cals)


        userFat = float(input('Enter fat grams'))
        userCarb = float(input('Enter carb grams'))
        userProtein = float(input('Enter protein grams'))
 

    users[name]["total"] = sum(users[name]["meals"])

print("Awesome! Let me tally everything up and see what it looks like!")


now = datetime.now()

print ("")
print ("       %s/%s/%s     " % (now.month, now.day, now.year))
print ("  ------------------")
print ("Name             Cals")
print ("  ------------------")
for name in users :
    print ("{}             {}".format(name, users[name]["total"]))
