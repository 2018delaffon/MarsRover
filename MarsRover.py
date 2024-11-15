class Rover:
    def __init__(self, name, xPosition, yPosition, direction):
        self.__name = name
        self.__xPosition = xPosition
        self.__yPosition = yPosition
        self.__direction = direction
        self.__instructions = ""
    def getXPosition(self):
        return self.__xPosition
    def getYPosition(self):
        return self.__yPosition
    def getDirection(self):
        return self.__direction
    def getInstructions(self):
        return self.__instructions
    def setXPosition(self, newXPosition):
        self.__xPosition = newXPosition
    def setYPosition(self, newYPosition):
        self.__yPosition = newYPosition
    def setDirection(self, newDirection):
        self.__direction = newDirection
    def setInstructions(self, newInstructions):
        self.__instructions = newInstructions

class Grid:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__colums = columns
    def getRows(self):
        return self.__rows
    def getColumns(self):
        return self.__columns
    def setRows(self, newX):
        self.__rows = newX
    def setColumns(self, newY):
        self.__columns = newY

### Validating user input ###
def userInput(rover, grid):
    valid = False
    while valid == False:
        print("Enter the current x coordinate of your rover")
        currentX = int(input())
        print("Enter the current y coordinate of your rover")
        currentY = int(input())
        print("Enter the starting direction")
        direction = input().upper()
        validDirection = ["N", "E", "S", "W"]
        if currentX <= grid.getRows() and currentY <= grid.getColumns() and direction in validDirection:
            valid = True
            rover.setXPosition(currentX)
            rover.setYPosition(currentY)
            rover.setDirection(direction)
        else:
            print("Not valid")

    valid = False
    while valid == False:
        print("Enter the instructions")
        instructions = input()
        validLetters = ["L", "M", "R"]
        count = 0
        for i in range(len(instructions)):
            if instructions[i] in validLetters:
                count = count + 1
        if count == len(instructions):
            valid = True
            rover.setInstructions(instructions)
        else:
            print("Not valid")

    print("Inputs Valid")

### Moving the rover forward ###
def moveForward(rover):
    direction = rover.getDirection()
    if direction == "N":
        y = rover.getYPosition()
        y = y + 1
        rover.setYPosition(y)
    elif direction == "E":
        x = rover.getXPosition()
        x = x + 1
        rover.setXPosition(x)
    elif direction == "S":
        y = rover.getYPosition()
        y = y - 1
        rover.setYPosition(y)
    else:
        x = rover.getXPosition()
        x = x - 1
        rover.setXPosition(x)

### Turning the rover left or right ###
def changeDirection(rover, turn):
    direction = rover.getDirection()
    if turn == "L":
        if direction == "N":
            rover.setDirection("W")
        elif direction == "E":
            rover.setDirection("N")
        elif direction == "S":
            rover.setDirection("E")
        else:
            rover.setDirection("S")
    else:
        if direction == "N":
            rover.setDirection("E")
        elif direction == "E":
            rover.setDirection("S")
        elif direction == "S":
            rover.setDirection("W")
        else:
            rover.setDirection("N")

### Processing the instructions ###
def roverInstructions(rover):
    instructions = rover.getInstructions()
    count = 0
    while count < len(instructions):
        if instructions[count] == "M":
            moveForward(rover)
        elif instructions[count] == "L":
            changeDirection(rover, "L")
        else:
            changeDirection(rover, "R")
        count = count + 1

### Main program ###
rover1 = Rover("Rover1", 0, 0, "N")
rover2 = Rover("Rover2", 0, 0, "N")
grid = Grid(0, 0)

### Check to see if the top corner is 5,5 ###
valid = False
while valid == False:
    print("Enter the furthest x coordinate of your grid")
    x = int(input())
    print("Enter the furthest y coordinate of your grid")
    y = int(input())
    if x == 5 and y == 5:
        valid = True
        grid.setRows(x)
        grid.setColumns(y)
    else:
        print("Not valid")

userInput(rover1, grid)
roverInstructions(rover1)
output1 = str(rover1.getXPosition()) + str(rover1.getYPosition()) + rover1.getDirection()
print(output1)

userInput(rover2, grid)
roverInstructions(rover2)
output2 = str(rover2.getXPosition()) + str(rover2.getYPosition()) + rover2.getDirection()
print(output2)
