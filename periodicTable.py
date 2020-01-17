from Tkinter import *
import random

window = Tk()
window.title("The Periodic Table Trivia")
window.geometry("750x750")

correct_guesses = 0
incorrect_guesses = 0

def random_number():
    global symbolBoxBtn
    choosenumber = 0
    choosenumber = random.randint(1, 5)
    symbolBoxBtn["text"] = choosenumber

def next_question():
    global entryBox
    new_letter = random_number()
    symbolBoxBtn["text"] = new_letter
    entryBox.delete(0, END)
    hintLbl["text"] = ""
    responseLbl.cget()




def submit_answer():
    global correct_guesses
    global incorrect_guesses
    userGuess = entryBox.get()
    userGuess = userGuess.upper()
    numberGenerated = symbolBoxBtn.cget('text')
    atomInfo = periodicTableDict.get(numberGenerated)
    atomSymbol = atomInfo[0]
    if atomSymbol == userGuess:
        responseLbl = Label(window, text="Correct")
        responseLbl.grid(row = 7, column = 2)
        correct_guesses += 1
        correctScoreLbl["text"] = "Correct guesses: " + str(correct_guesses)
    else:
        incorrect_guesses += 1
        responseLbl = Label(window, text="Incorrect")
        incorrectScoreLbl["text"] = "Incorrect guesses: " + str(incorrect_guesses)
        responseLbl.grid(row = 7, column = 2)



def hint_button():
    numberGenerated = symbolBoxBtn.cget('text')
    atomInfo = periodicTableDict.get(numberGenerated)
    atomName = atomInfo[1]
    hintLbl["text"] = atomName


periodicTableDict = {
    1: ["H", "Hydrogen"],
    2: ["HE", "HELIUM"],
    3: ["LI", "LITHIUM"],
    4: ["BE", "BERYLLIUM"],
    5: ["B", "BORON"]
}

symbolBoxBtn = Button(window, text="")
symbolBoxBtn.grid(row=0, column=2)
symbolBoxBtn["command"] = random_number()

correctScoreLbl = Label(window, text="Correct guesses: " + str(correct_guesses))
correctScoreLbl.grid(row=1, column=0)

incorrectScoreLbl = Label(window, text="Incorrect guesses: " + str(incorrect_guesses))
incorrectScoreLbl.grid(row=2, column=0)

entryBox = Entry(window, width=50)
entryBox.grid(row=4, column=2)
# entryBox.pack()

submitAnswerBtn = Button(window, text="Submit Answer", command=submit_answer)
submitAnswerBtn.grid(row=5, column=2)

hintBtn = Button(window, text="Hint", command=hint_button)
hintBtn.grid(row=6, column=2)

directionsLbl = Label(window, text="What is the atomic symbol for this number?")
directionsLbl.grid(row=2, column=2)

newSymbol = Button(window, text = "Next >", command = next_question)
newSymbol.grid(row=7, column=4)

hintLbl = Label(window, text="")
hintLbl.grid(row=9, column=2)

if incorrect_guesses == 5:
    incorrect_guesses = 0
    correct_guesses = 0

window.mainloop()
