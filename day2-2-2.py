print("Advent of Code 2019 - Day 2 Part 2 v2")


class IntegerCode():
    def loadMemoryFromFile(self):
        for line in open('day2-input.txt'):
            self.memory = [int(x) for x in line.split(',')]

    def changeInput(self, inputOne, inputTwo):
        self.memory[1] = inputOne
        self.memory[2] = inputTwo

    def run(self):
        currentIndex = 0

        while (currentIndex <= len(self.memory)):
            # print("Current instruction: ", array[current], " at index: ", current)
            if self.memory[currentIndex] == 1:
                self.processInstructionOne(currentIndex)
            elif self.memory[currentIndex] == 2:
                self.processInstructionTwo(currentIndex)
            elif self.memory[currentIndex] == 99:
                return self.memory[0]
            else:
                print("INVALID INSTRUCTION, EXITING")
                return -1

            currentIndex += 4

        print("REACHED END OF FILE WITHOUT EXITING")
        return -1

    def processInstructionOne(self, index):
        firstValue = self.memory[self.memory[index + 1]]
        secondValue = self.memory[self.memory[index + 2]]
        valueToWrite = firstValue + secondValue
        indexToWrite = self.memory[index + 3]
        self.memory[indexToWrite] = valueToWrite

    def processInstructionTwo(self, index):
        firstValue = self.memory[self.memory[index + 1]]
        secondValue = self.memory[self.memory[index + 2]]
        valueToWrite = firstValue * secondValue
        indexToWrite = self.memory[index + 3]
        self.memory[indexToWrite] = valueToWrite


# Bruteforce our way through all possible inputs
for inputOne in range(0, 99):
    for inputTwo in range(0, 99):
        program = IntegerCode()
        program.loadMemoryFromFile()
        program.changeInput(inputOne, inputTwo)
        output = program.run()

        if output == 19690720:
            answer = (100 * inputOne) + inputTwo
            print("Got the solution! Input one: ", inputOne,
                  "Input two: ", inputTwo, "Answer: ", answer)
            exit()
