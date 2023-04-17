
class PDA:
    def __init__(self, stackLang, terminalLang, transitions, start, accepting, states):
        self.stack = []
        self.stackLang = stackLang
        self.terminalLang = terminalLang
        self.transitions = transitions
        self.startState = start
        self.acceptingStates = accepting
        self.states = states

    # todo: finish/organize methods. Delete any not needed
    def getStartState(self):
        return self.startState

    def getStackLen(self):
        return len(self.stack)

    def getStackHead(self):
        if len(self.stack) == 0:
            return ''
        else:
            return self.stack[-1]

    def setHead(self, head):
        if head == '':
            pass
        else:
            self.stack.append(head)

    def stackPop(self):
        self.stack.pop()


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
        # todo: make run for empty strings

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
    # return True/False bool value if accepted true

    currentState = pda.getStartState()
    processedStr = 0
    while True:
        if processedStr == len(string):  # only possible transitions are with null string
            if currentState in pda.acceptingStates and pda.getStackLen() == 0:
                return True
            else:
                value = None
                try:
                    value = pda.transitions[(currentState, '', pda.getStackHead())]
                except KeyError:
                    pass

                if value is not None:
                    currentState = value[0]
                    pda.setHead(value[1])
                    if pda.getStackHead() != '':
                        pda.stackPop()
                else:  # no transitions possible
                    return False
        else:
            # string not processed still
            value = None
            char = None
            try:
                value = pda.transitions[(currentState, string[processedStr], pda.getStackHead())]
                char = 1
            except KeyError:
                pass

            try:
                value = pda.transitions[(currentState, string[processedStr], '')]
                char = 1
            except KeyError:
                pass

            try:
                value = pda.transitions[(currentState, '', pda.getStackHead())]
            except KeyError:
                pass

            if value is not None:
                if pda.getStackHead() != '':
                    pda.stackPop()
                currentState = value[0]
                pda.setHead(value[1])
                if char is not None:
                    processedStr += 1

            else:
                return False


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
