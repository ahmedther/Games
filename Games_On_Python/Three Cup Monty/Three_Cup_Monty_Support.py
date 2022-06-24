from random import Random

"""
    Support file for the actual game all methods and functions will be added here.
    
    Note!!! cannot use "with" function as __enter__ and __exit__ method is missing

"""

# this will inherit all the fucrions of Random class
class tcms(Random):
    def __init__(
        self,
    ):
        super(tcms, self).__init__()

        """Constructor"""

    # shuffel the monty
    def shuffbase(self, baselist=["", 0, ""]):
        self.shuffle(baselist)
        return baselist

    # get the guess from user / player
    def userinput(self):
        self.input = ""
        while self.input not in ["1", "2", "3"]:
            self.input = input("\nPlease enter a valid number in range of 1 to 3\n")

        else:
            uinput = int(self.input) - 1
            return uinput

    # Show / print the results to the user
    def results(self, baselist, uinput):
        self.baselist = baselist
        self.uinput = uinput
        if baselist[uinput] == 0:
            print(f"\nThat is correct!!! The 0 was in {baselist}\n")

        else:
            print(f"\nIncorrect!!! it was in {baselist} \n")


if __name__ == "__main__":
    tcms()
