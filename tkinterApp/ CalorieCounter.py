
import tkinter as tk
import datetime

window = tk.Tk() #the window variable now has all the properties of tkinter

window.title("DAILY CALORIE COUNTER", font=("times 30 bold italic"), fg=("#FFC0CB"))

window.geometry("400x400")

#TITLE
def welcome():
	title = tk.Label(text = 'WELCOME TO CALORIE COUNTER!!! \n it is quite simple: \n just put in calories from your meals and get the results of your daily intake!', font=("times 24 bold italic"), fg=("#FFC0CB"))
	title.grid(column=0, row=1)


def numofpeople():
#NUMBER OF PEOPLE!
	Label1 = tk.Label(text = "How Many Users In Total?",font=("times 18 bold "), fg=("#ff879c"))
	Label1.grid(column=0, row=1)
	#Entry for # of ppl
	entryField1 = tk.Entry()
	entryField1.grid(column=1, row=1)


def breakfast():
#CALORIES FOR BREAKFAST
	Label2 = tk.Label(text = "How many breakfast calories:",font=("times 18 bold "), fg=("#bed0ff"))
	Label2.grid(column=0, row=2)
	#input for number of calories for breakfast!
	entryField2 = tk.Entry()
	entryField2.grid(column=1, row=2)

def brunch():
#CALORIES FOR BRUNCH
	Label3 = tk.Label(text = "How many brunch calories:",font=("times 18 bold "), fg=("#b07eff"))
	Label3.grid(column=0, row=3)

	entryField3 = tk.Entry()
	entryField3.grid(column=1, row=3)

def lunch():
#CALORIES FOR LUNCH
	Label4 = tk.Label(text = "How many lunch calories:",font=("times 18 bold "), fg=("#b07eff"))
	Label4.grid(column=0, row=4)

	entryField4 = tk.Entry()
	entryField4.grid(column=1, row=4)

def snack():
#CALORIES FOR SNACK
	Label5 = tk.Label(text = "How many snack calories:",font=("times 18 bold "), fg=("#b07eff"))
	Label5.grid(column=0, row=5)

	entryField5 = tk.Entry()
	entryField5.grid(column=1, row=5)

def dinner():
#CALORIES FOR DINNER
	Label6 = tk.Label(text = "How many dinner calories:",font=("times 18 bold "), fg=("#b07eff"))
	Label6.grid(column=0, row=6)

	entryField6 = tk.Entry()
	entryField6.grid(column=1, row=6)

window.mainloop() #runs everything inside window


