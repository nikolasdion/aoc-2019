print("Advent of Code 2019 - Day 1 Part 1")


def fuelForMass(mass):
    return (mass // 3) - 2


fuelTotal = 0

for line in open("day1-input.txt"):
    mass = int(line)
    fuelTotal += fuelForMass(mass)

print(fuelTotal)
