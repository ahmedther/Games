# Code for Hangman
theword = "Chabutra"
lettergussed = ""
# Simple version of the game Hangman 
turns = input(
    "Type, Easy for easy mode with (9 turns)\nNormal for normal mode (6 turns)\nHard for hard mode (3 turns)\nGod for God Level Diffculty (1 Turn)\nWrite I am a toddler to choose you are own number of turns\n Please note this is a case sensitive input so make sure fisrt letter you enter is in capital :p\n"
)
if turns == "Easy":
    turns = 9
elif turns == "Normal":
    turns = 6
elif turns == "Hard":
    turns = 3
elif turns == "God":
    turns = 1
elif turns == "I am a toddler":
    turns = input("Please enter your own number of turns you fucking toddler ")
    turns = int(turns)
else:
    print(
        "Please enter a correct value given from the list"
    )

while turns > 0:
    guess = input(" Take a guess and enter a Alphabet  ")
    if guess in theword:
        print(f"Thats Correct!\n{guess} matches in the secet word :D")
    else:
        turns -= 1
        print(f"EEEH!! Thats Incorrect\nTry again, you have {turns} turns left.")

    lettergussed = lettergussed + guess

    wrongtries = 0

    for letter in theword:
        if letter in lettergussed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongtries += 1
    if wrongtries == 0:
        print(
            f"Congratulations!!!\nYou have sucessfully found all the words in {theword}\nYou WON!!!"
        )
        break

else:
    print(
        f"Is this the best you can do?\nYou have exhausted all your tries and you only managed to get {lettergussed}?\n Try again next, maybe in toddler mode."
    )
