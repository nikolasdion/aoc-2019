print("Advent of Code 2019 - Day 2 Part 1")


def intCode(array):
    current = 0

    while (current < len(array)):
        print("Current instruction: ", array[current], " at index: ", current)
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
            return array
        else:
            print("INVALID INSTRUCTION, EXITING")
            return array

        current += 4


def restoreTo1202(array):
    array[1] = 12
    array[2] = 2
    return array


def loadInputFile():
    for line in open('day2-input.txt'):
        stringArray = line.split(',')
        intArray = [int(x) for x in stringArray]
        return intArray


restoredArray = restoreTo1202(loadInputFile())
outputArray = intCode(restoredArray)

print(outputArray[0])
