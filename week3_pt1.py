def calculateCalFromFat(fatGram):
    CalFromFat = fatGram * 9 
    return CalFromFat

def calculateCalFromCarb(carbGram): 
    CalFromCarb = carbGram * 4
    return CalFromCarb

def calculateCalFromProtein (proteinGram):
    CalFromProtein = proteinGram * 4
    return CalFromProtein

def total (CalFromFat, calculateCalFromCarb, CalFromProtein):
    TotalOfCalories = CalFromFat+CalFromCarb+CalFromProtein

def main(): 
    userFat = float(input('Enter fat grams'))
    userCarb = float(input('Enter carb grams'))
    userProtein = float(input('Enter protein grams'))

    CFF = calculateCalFromFat(userFat)
    CCC = calculateCalFromCarb(userCarb)
    CCP = calculateCalFromProtein(userProtein)
