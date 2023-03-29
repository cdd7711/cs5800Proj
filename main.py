
class PDA:
    def __init__(self, stackLang, terminalLang, transitions, start, accepting, states):
        self.stack = []
        self.stackLang = stackLang
        self.terminalLang = terminalLang
        self.transitions = transitions
        self.startState = start
        self.acceptingStates = accepting
        self.states = states
        self.currentState = self.startState

    # todo: finish/organize methods

    # getStackLang might not be needed
    def getStackLang(self):  # maybe make this a function that takes a char and returns if it is an element of the stack string?
        return self.stackLang

    def getStackHead(self):
        return self.stack[-1]

    def stackAppend(self, char):
        # adds to stack (at end of the list)
        self.stack.append(char)

    def stackPop(self):
        # todo: do we want to make this a function that tests if you can pop (a given char) and returns T/F if popped?
        self.stack.pop()

    def inAccepting(self, state):
        # todo: return if state is in self.acceptingStates

    def setState(self, state):
        self.currentState = state

def main():
    # gets, validates, and opens PDA file
    while True:
        try:
            pdaFile = open(input("What PDA text file do you want to open?\n"), "r")
            break
        except FileNotFoundError:
            print("That is not a valid file name.")

    # gets, validates, and opens string file
    while True:
        try:
            stringFile = open(input("What string text file do you want to open?\n"), "r")
            break
        except FileNotFoundError:
            print("That is not a valid file name.")

    pdaClass = fillPDA(pdaFile)

    # todo: for each line in string file, send PDA and string to runPDA

    # close files
    pdaFile.close()
    stringFile.close()


def runPDA(pda, string):
    # todo: fill this in recursively to run through the given PDA with a string
    # todo: print if accepted/not accepted


def fillPDA(pdaFile):
    # organize a text file to have start state, accepting states, transitions, stack language, terminal language

    states = pdaFile.readline().split(",")  # list
    terminalLang = pdaFile.readline().split(",")  # list
    stackLang = pdaFile.readline().split(",")  # list
    accepting = pdaFile.readline().split(",")  # list
    start = pdaFile.readline().strip("\n")  # list

    # todo: rest of file is transitions. Read these into dictionary transitions

    pdaClass = PDA(stackLang, terminalLang, transitions, start, accepting, states)

    return pdaClass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
