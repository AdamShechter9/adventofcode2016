# Adam Shechter
# Advent of code
# day 10
import re


class bots(object):

    def __init__(self, rawIn):
        self.instructions = rawIn.split('\n')
        self.instructions.pop(len(self.instructions)-1)
        self.minbot, self.maxbot = self.minbotmaxbot(rawIn)
        self.minout, self.maxout = self.minoutmaxout(rawIn)
        self.simulation, self.outputs = self.initializeScene()

    def minbotmaxbot(self, rawInstructions):
        print("Searching for low and high bot numbers")
        minbot = -1
        maxbot = -1

        botlist = re.findall(r'bot\s(\d+)',rawInstructions)
        for bot in botlist:
            bot = int(bot)
            if minbot == -1 and maxbot == -1:
                minbot = bot
                maxbot = bot
            else:
                if bot < minbot:
                    minbot = bot
                elif bot > maxbot:
                    maxbot = bot
        print("max bot: "+str(maxbot))
        print("min bot: "+str(minbot))
        return minbot, maxbot

    def minoutmaxout(self, rawInstructions):
        print("Searching for low and high out numbers")
        minout = -1
        maxout = -1

        outlist = re.findall(r'output\s(\d+)',rawInstructions)
        for out in outlist:
            out = int(out)
            if minout == -1 and maxout == -1:
                minout = out
                maxout = out
            else:
                if out < minout:
                    minout = out
                elif out > maxout:
                    maxout = out
        print("max out: "+str(maxout))
        print("min out: "+str(minout))
        return minout, maxout

    def initializeScene(self):
        print("creating init scene")
        simulation = []
        outputs = []
        for index in range(self.minbot, self.maxbot+1):
            simulation.insert(index, [])
        for jndex in range(self.minout, self.maxout+1):
            outputs.insert(index, [])
        return simulation, outputs

    def runBots(self):
        completeLoop = False
        doneCommands = []
        while not completeLoop:
            completeLoop = True
            for currinstr in self.instructions:
                if currinstr in doneCommands:
                    continue
                instr = currinstr.strip().split()
                if instr[0] == "value":
                    # add value to numbered bot
                    currbot = int(instr[5])
                    value = int(instr[1])
                    self.simulation[currbot].append(value)
                    completeLoop = False
                    doneCommands.append(currinstr)
                elif instr[0] == "bot":
                    src = int(instr[1])
                    isLowOutput = True if instr[5] == "output" else False
                    isHiOutput = True if instr[10] == "output" else False
                    lowdest = int(instr[6])
                    hidest = int(instr[11])
                    if len(self.simulation[src]) > 1:
                        self.simulation[src].sort()
                        hi = self.simulation[src].pop()
                        lo = self.simulation[src].pop()
                        if isHiOutput:
                            self.outputs[hidest].append(hi)
                        else:
                            self.simulation[hidest].append(hi)
                        if isLowOutput:
                            self.outputs[lowdest].append(lo)
                        else:
                            self.simulation[lowdest].append(lo)
                        completeLoop = False
                        doneCommands.append(currinstr)
                        if lo == 17 and hi == 61:
                            print("bot "+str(src)+" compared 17 with 61")
        return

def main():
    test1 = "value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2\n"
    test2 = ""

    with open("input.txt", "r") as f:
        test2 = f.read()

    mybots = bots(test2)
    mybots.runBots()

    print(mybots.simulation)
    print(mybots.outputs)
if __name__=='__main__':
    main()
