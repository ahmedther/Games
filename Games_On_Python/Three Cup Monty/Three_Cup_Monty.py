from Three_Cup_Monty_Support import tcms

"""
Small game and code but really shows the core of object oriented progamming

"""
# Games allways run on loops
Loop = True

while Loop is True:

    tc = tcms()

    monty = tc.shuffbase()

    get_user_guess = tc.userinput()

    tc.results(monty, get_user_guess)

    # option for user to get out of the game / loop
    uinput = input(
        "\nDo You want to exit the game\n Press enter 'Yes' to exit, or press any button to continue\n"
    )

    if uinput in ["yes", "YES", "Yes"]:
        break

    else:
        pass
