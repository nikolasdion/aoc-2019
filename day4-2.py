def same_two_adjacent_digits(number: int):
    number_str = str(number)
    next_digit_to_check = 0

    while(next_digit_to_check < len(number_str) - 1):
        if number_str[next_digit_to_check] == number_str[next_digit_to_check + 1]: return True
        next_digit_to_check =+ 1

    for i in range(len(number_str) - 1):
        if number_str[i] == number_str[i + 1]: return True

    return False


def digits_never_decrease(number: int):
    number_str = str(number)

    for i in range(len(number_str) - 1):
        if int(number_str[i]) > int(number_str[i + 1]): return False
    
    return True

def meets_criteria(number: int):
    return same_two_adjacent_digits(number) and digits_never_decrease(number)

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 4 part 2")

    # Test 124075-580769
    rangeToTest = range(124075, 580770)

    count = 0

    for number in rangeToTest:
        if meets_criteria(number): count += 1
    
    print("Number of passwords that meet criteria:", count)





