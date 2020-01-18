from Tkinter import *
import random

window = Tk()
window.title("The Periodic Table Trivia")
window.geometry("750x750")
restartVar = ""

correct_guesses = 0
incorrect_guesses = 0

def random_number():
    global symbolBoxBtn
    choosenumber = 0
    choosenumber = random.randint(1, 5)
    symbolBoxBtn["text"] = choosenumber

def next_question():
    global entryBox
    global responseLbl
    new_letter = random_number()
    symbolBoxBtn["text"] = new_letter
    entryBox.delete(0, END)
    hintLbl["text"] = ""
    restartLbl["text"] = ""
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
        if incorrect_guesses == 5:
            incorrect_guesses = 0
            correct_guesses = 0
            restartLbl["text"] = "You Lost. Resetting Score."



def hint_button():
    numberGenerated = symbolBoxBtn.cget('text')
    atomInfo = periodicTableDict.get(numberGenerated)
    atomName = atomInfo[1]
    hintLbl["text"] = atomName


periodicTableDict = {
    1: ["H", "Hydrogen"],
    2: ["He", "Helium"],
    3: ["Li", "Lithium"],
    4: ["Be", "Beryllium"],
    5: ["B", "Boron"],
    6: ["C", "Carbon"],
    7: ["N", "Nitrogen"],
    8: ["O", "Oxygen"],
    9: ["F", "Fluorine"],
    10: ["Ne", "Neon"],
    11: ["Na", "Sodium"],
    12: ["Mg", "Magnesium"],
    13: ["Al", "Aluminium"],
    14: ["Si", "Silicon"],
    15: ["P", "Phosphorus"],
    16: ["S", "Sulfur"],
    17: ["Cl", "Chlorine"],
    18: ["Ar", "Argon"],
    19: ["K", "Potassium"],
    20: ["Ca", "Calcium"],
    21: ["Sc", "Scandium"],
    22: ["Ti", "Titanium"],
    23: ["V", "Vanadium"],
    24: ["Cr", "Chromium"],
    25: ["Mn", "Manganese"],
    26: ["Fe", "Iron"],
    27: ["Co", "Cobalt"],
    28: ["Ni", "Nickel"],
    29: ["Cu", "Copper"],
    30: ["Zn", "Zinc"],
    31: ["Ga", "Gallium"],
    32: ["Ge", "Germanium"],
    33: ["As", "Arsenic"],
    34: ["Se", "Selenium"],
    35: ["Br", "Bromine"],
    36: ["Kr", "Krypton"],
    37: ["Rb", "Rubidium"],
    38: ["Sr", "Strontium"],
    39: ["Y", "Yttrium"],
    40: ["Zr", "Zirconium"],
    41: ["Nb", "Niobium"],
    42: ["Mo", "Molybdenum"],
    43: ["Tc", "Technetium"],
    44: ["Ru", "Ruthenium"],
    45: ["Rh", "Rhodium"],
    46: ["Pd", "Palladium"],
    47: ["Ag", "Silver"],
    48: ["Cd", "Cadmium"],
    49: ["In", "Indium"],
    50: ["Sn", "Tin"],
    51: ["Sb", "Antimony"],
    52: ["Te", "Tellurium"],
    53: ["I", "Iodine"],
    54: ["Xe", "Xenon"],
    55: ["Cs", "Cesium"],
    56: ["Ba", "Barium"],
    57: ["La", "Lanthanum"],
    58: ["Ce", "Cerium"],
    59: ["Pr", "Praseodymium"],
    60: ["Nd", "Neodymium"],
    61: ["Pm", "Promethium"],
    62: ["Sm", "Samarium"],
    63: ["Eu", "Europium"],
    64: ["Gd", "Gadolinium"],
    65: ["Tb", "Terbium"],
    66: ["Dy", "Dysprosium"],
    67: ["Ho", "Holmium"],
    68: ["Er", "Erbium"],
    69: ["Tm", "Thulium"],
    70: ["Yb", "Ytterbium"],
    71: ["Lu", "Lutetium"],
    72: ["Hf", "Hafnium"],
    73: ["Ta", "Tantalum"],
    74: ["W", "Tungsten"],
    75: ["Re", "Rhenium"],
    76: ["Os", "Osmium"],
    77: ["Ir", "Iridium"],
    78: ["Pt", "Platinum"],
    79: ["Au", "Gold"],
    80: ["Hg", "Mercury"],
    81: ["Tl", "Thallium"],
    82: ["Pb", "Lead"],
    83: ["Bi", "Bismuth"],
    84: ["Po", "Polonium"],
    85: ["At", "Astatine"],
    86: ["Rn", "Radon"],
    87: ["Fr", "Francium"],
    88: ["Ra", "Radium"],
    89: ["Ac", "Actinium"],
    90: ["Th", "Thorium"],
    91: ["Pa", "Protactinium"],
    92: ["U", "Uranium"],
    93: ["Np", "Neptunium"],
    94: ["Pu", "Plutonium"],
    95: ["Am", "Americium"],
    96: ["Cm", "Curium"],
    97: ["Bk", "Berkelium"],
    98: ["Cf", "Californium"],
    99: ["Es", "Einsteinium"],
    100: ["Fm", "Fermium"],
    101: ["Md", "Mendelevium"],
    102: ["No", "Nobelium"],
    103: ["Lr", "Lawrencium"],
    104: ["Rf", "Rutherfordium"],
    105: ["Db", "Dubnium"],
    106: ["Sg", "Seaborgium"],
    107: ["Bh", "Bohrium"],
    108: ["Hs", "Hassium"],
    109: ["Mt", "Meitnerium"],
    110: ["Ds", "Darmstadtium"],
    111: ["Rg", "Roentgenium"],
    112: ["Cn", "Copernicium"],
    113: ["Nh", "Nihonium"],
    114: ["Fl", "Flerovium"],
    115: ["Mc", "Moscovium"],
    116: ["Lv", "Livermorium"],
    117: ["Ts", "Tennessee"],
    118: ["Og", "Oganesson"]
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

newSymbol = Button(window, text = "Next ->", command = next_question)
newSymbol.grid(row=7, column=4)

hintLbl = Label(window, text="")
hintLbl.grid(row=9, column=2)

restartLbl = Label(window, text = restartVar)
restartLbl.grid(row = 3, column = 0)



window.mainloop()
