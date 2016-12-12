#Adam Shechter
#Advent of code day 8

WIDTH = 50
HEIGHT = 6
#WIDTH = 7
#HEIGHT = 3


class LCDScreen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        row = []
        for i in range(width):
            row.append(0)
        self.grid = []
        for j in range(height):
            newRow = row[:]
            self.grid.append(newRow)


    def run(self, instruction):
        print("instruction: "+instruction)
        if instruction[0:4] == 'rect':
            rawInput = instruction.split()
            rawInput = rawInput[1].split('x')
            w = int(rawInput[0])
            h = int(rawInput[1])
            print("rect command "+str(w)+" "+str(h))
            for row in range(h):
                for col in range(w):
                    #print(col,row)
                    self.grid[row][col] = 1
                    #print(self.grid)

        elif instruction[0:13] == 'rotate column':
            rawInput = instruction.split()
            rawInput2 = rawInput[2].split('=')
            col = int(rawInput2[1])
            steps = int(rawInput[4])
            print("rotate column "+str(col)+" "+str(steps))
            for step in range(steps):
                temp2 = self.grid[self.height-1][col]
                for row in range(self.height):
                    temp = self.grid[row][col]
                    self.grid[row][col] = temp2
                    temp2 = temp

        elif instruction[0:10] == 'rotate row':
            rawInput = instruction.split()
            rawInput2 = rawInput[2].split('=')
            row = int(rawInput2[1])
            steps = int(rawInput[4])
            print("rotate row "+str(row)+" "+str(steps))
            for step in range(steps):
                temp2 = self.grid[row][self.width-1]
                for col in range(self.width):
                    temp = self.grid[row][col]
                    self.grid[row][col] = temp2
                    temp2 = temp

    def reportCount(self):
        count = 0
        for col in range(self.width):
            for row in range(self.height):
                if self.grid[row][col] == 1:
                    count += 1
        return count

    def displayGrid(self):
        bufferStr = ""
        print()
        print("*************************************************************")
        print()
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 1:
                    bufferStr += '*'
                else:
                    bufferStr += ' '
            print(bufferStr)
            bufferStr = ""

        return

def main():
    test1 = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=0 by 4",
    "rotate column x=1 by 1"
    ]
    test2 = []

    with open("input.txt", "r") as f:
        fdata = f.readlines()
        for line in fdata:
            data = line.strip()
            test2.append(data)

    screen1 = LCDScreen(WIDTH, HEIGHT)
    print("initialized")
    print(screen1.grid)

    for instruction in test2:
        screen1.run(instruction)
        print(screen1.grid)

    print("On's: "+ str(screen1.reportCount()))
    print()
    screen1.displayGrid()
if __name__ == '__main__':
    main()
