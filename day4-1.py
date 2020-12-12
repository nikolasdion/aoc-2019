def same_two_adjacent_digits(number: int):
    numberStr = str(number)

    for i in range(len(numberStr) - 1):
        if numberStr[i] == numberStr[i + 1]: return True

    return False

def digits_never_decrease(number: int):
    numberStr = str(number)

    for i in range(len(numberStr) - 1):
        if int(numberStr[i]) > int(numberStr[i + 1]): return False
    
    return True

def meets_criteria(number: int):
    return same_two_adjacent_digits(number) and digits_never_decrease(number)

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 4 part 1")

    # Test 124075-580769
    rangeToTest = range(124075, 580770)

    count = 0

    for number in rangeToTest:
        if meets_criteria(number): count += 1
    
    print("Number of passwords that meet criteria:", count)





