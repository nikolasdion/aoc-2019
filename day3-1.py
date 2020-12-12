print("Advent of Code 2019 - Day 3 part 1")


class HorizontalLine:
    def __init__(self, y: int, x_start: int, x_finish: int):
        self.y = y
        # +1 because we don't count the starting point and ending point
        self.x_range = range(x_start + 1, x_finish)


class VerticalLine:
    def __init__(self, x: int, y_start: int, y_finish: int):
        self.x = x
        # +1 because we don't count the starting point and ending point
        self.y_range = range(y_start + 1, y_finish)


def intersects(horizontal_line: HorizontalLine, vertical_line: VerticalLine):
    return horizontal_line.y in vertical_line.y_range and vertical_line.x in horizontal_line.x_range


def intersection_manhattan_distance(horizontal_line: HorizontalLine, vertical_line: VerticalLine):
    if intersects(horizontal_line, vertical_line):
        return abs(horizontal_line.y) + abs(vertical_line.x)
    else:
        return -1


class Wire:
    # Start at 0,0
    current_x = 0
    current_y = 0

    horizontal_lines = []
    vertical_lines = []

    def processInstruction(self, instructionStr: str):
        # First character is the
        direction = instructionStr[0]
        distance = int(instructionStr[1:])

        # print(direction, distance)

        if (direction == 'U'):
            newLine = VerticalLine(
                self.current_x, self.current_y, self.current_y + distance)
            self.vertical_lines.append(newLine)
            self.current_y += distance
        elif (direction == 'D'):
            newLine = VerticalLine(
                self.current_x, self.current_y - distance, self.current_y)
            self.vertical_lines.append(newLine)
            self.current_y -= distance
        elif (direction == 'R'):
            newLine = HorizontalLine(
                self.current_y, self.current_x, self.current_x + distance)
            self.horizontal_lines.append(newLine)
            self.current_x += distance
        elif(direction == 'L'):
            newLine = HorizontalLine(
                self.current_y, self.current_x - distance, self.current_x)
            self.horizontal_lines.append(newLine)
            self.current_x -= distance
        else:
            print("INVALID DIRECTION:", direction)

    def processInstructions(self, instructions):
        for instruction in instructions:
            self.processInstruction(instruction)


def closest_intersections(wire_one: Wire, wire_two: Wire):
    all_intersections = []

    for one_vertical in wire_one.vertical_lines:
        for two_horizontal in wire_two.horizontal_lines:
            intersection_distance = intersection_manhattan_distance(
                two_horizontal, one_vertical)
            if (intersection_distance > 0):
                print("Found intersection 1:", intersection_distance)
                all_intersections.append(intersection_distance)

    for one_horizontal in wire_one.horizontal_lines:
        for two_vertical in wire_two.vertical_lines:
            intersection_distance = intersection_manhattan_distance(
                one_horizontal, two_vertical)
            if (intersection_distance > 0):
                print("Found intersection 2:", intersection_distance)
                all_intersections.append(intersection_distance)

    return min(all_intersections)


wire_one = Wire()
wire_two = Wire()

instructions_one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
instructions_two = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

wire_one.processInstructions(instructions_one)
wire_two.processInstructions(instructions_two)

print(closest_intersections(wire_one, wire_two))
