print("Advent of Code 2019 - Day 1 Part 2")


def fuelForMass(mass):
    # "//"" is floor division
    fuel = (mass//3) - 2

    if (fuel <= 0):
        return 0
    else:
        return fuel + fuelForMass(fuel)


fuelTotal = 0

for line in open('day1-input.txt'):
    moduleMass = int(line)
    fuelForModule = fuelForMass(moduleMass)
    fuelTotal += fuelForMass(moduleMass)

print(fuelTotal)
