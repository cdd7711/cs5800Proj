
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

    # todo: finish/organize methods. Delete any not needed

    # getStackLang might not be needed
    def getStackLang(self):
    # maybe make this a function that takes a char and returns if it is an element of the stack string?
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
    # gets, validates, and opens PDA file. same pda file for each string
    while True:
        try:
            pdaFile = open(input("What PDA text file do you want to open?\n"), "r")
            break
        except FileNotFoundError:
            print('That is not a valid file name. An example file is "pg224.txt"')

    # gets, validates, and opens string file
    while True:
        try:
            stringFile = open(input("What string text file do you want to open?\n"), "r")
            break
        except FileNotFoundError:
            print('That is not a valid file name. An example file is "strings.txt"')

    # for each line in string file, send PDA and string to runPDA
    for line in stringFile:
        pdaClass = fillPDA(pdaFile)
        result = runPDA(pdaClass, line.strip("\n"))
        if result is True:
            print("Your PDA with string", line.strip("\n"), "was accepted.")
        else:
            print("Your PDA with string", line.strip("\n"), "was NOT accepted.")

    # close files
    pdaFile.close()
    stringFile.close()


def runPDA(pda, string):
    # todo: fill this in recursively to run through the given PDA (class) with a string
    # todo: return True/False bool value if accepted true
    # todo: Possibly test that each terminal and stack char are elements of their languages


def fillPDA(pdaFile):
    # organize a text file to have start state, accepting states, transitions, stack language, terminal language

    states = pdaFile.readline().strip("\n").split(",")  # list
    terminalLang = pdaFile.readline().strip("\n").split(",")  # list
    stackLang = pdaFile.readline().strip("\n").split(",")  # list
    accepting = pdaFile.readline().strip("\n").split(",")  # list
    start = pdaFile.readline().strip("\n")  # list

    transitions = {}  # dict with tuple: tuple
    # key is (start state, terminal, stack head to pop)
    # value is (new state, new stack head pushed)

    line = pdaFile.readline()
    while line:
        line = line.strip("\n").split(",")
        key = (line[0], line[1], line[2])
        value = (line[3], line[4])
        transitions[key] = value

        line = pdaFile.readline()

    return PDA(stackLang, terminalLang, transitions, start, accepting, states)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
