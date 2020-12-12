print("Advent of Code 2019 - Day 2 Part 1")

class IntegerCode():
    def loadMemoryFromFile(self):
        self.memory = loadInputFile()

    def changeInput(self, inputOne, inputTwo):
        self.memory[1] = inputOne
        self.memory[2] = inputTwo

    def run(self, parameter_list):
        pass


def intCode(array):
    current = 0

    while (current < len(array)):
        # print("Current instruction: ", array[current], " at index: ", current)
        if array[current] == 1:
            firstValue = array[array[current + 1]]
            secondValue = array[array[current + 2]]
            valueToWrite = firstValue + secondValue
            indexToWrite = array[current + 3]
            array[indexToWrite] = valueToWrite
        elif array[current] == 2:
            firstValue = array[array[current + 1]]
            secondValue = array[array[current + 2]]
            valueToWrite = firstValue * secondValue
            indexToWrite = array[current + 3]
            array[indexToWrite] = valueToWrite
        elif array[current] == 99:
            return array[0]
        else:
            print("INVALID INSTRUCTION, EXITING")
            return -1

        current += 4


def changeInput(array, inputOne, inputTwo):
    newArray = array
    newArray[1] = inputOne
    newArray[2] = inputTwo
    return newArray

def loadInputFile():
    for line in open('day2-input.txt'):
        stringArray = line.split(',')
        intArray = [int(x) for x in stringArray]
        return intArray

originalArray = loadInputFile()

# Bruteforce our way through all possible inputs
for inputOne in range (0, 99):
    for inputTwo in range (0, 99):
        inputArray = changeInput(loadInputFile(), inputOne, inputTwo)
        output = intCode(inputArray)
        if output == 19690720:
            answer = (100 * inputOne) + inputTwo
            print("Got the solution! Input one: ", inputOne, "Input two: ", inputTwo, "Answer: ", answer)
            exit()

        

