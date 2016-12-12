#Adam Shechter
#Advent of code day 6

def repetitionCodeA(inputMatrix):
    messageOut = []

    for col in range(len(inputMatrix[0])):
        letterMap = {}
        for row in range(len(inputMatrix)):
            testChr = inputMatrix[row][col]
            try:
                letterMap[testChr] += 1
            except KeyError:
                letterMap[testChr] = 1

        sortMap = sorted(letterMap.items(), key=lambda x: x[1], reverse=True)
        #freqMap = sorted(chrMap.items(), key=lambda x: x[1], reverse=True)

        print(sortMap)
        chrMax, value = sortMap[0]
        print(str(chrMax)+' '+str(value))
        messageOut.append(chrMax)


    return "".join(messageOut)

def repetitionCodeB(inputMatrix):
    messageOut = []

    for col in range(len(inputMatrix[0])):
        letterMap = {}
        for row in range(len(inputMatrix)):
            testChr = inputMatrix[row][col]
            try:
                letterMap[testChr] += 1
            except KeyError:
                letterMap[testChr] = 1

        sortMap = sorted(letterMap.items(), key=lambda x: x[1])
        #freqMap = sorted(chrMap.items(), key=lambda x: x[1], reverse=True)

        print(sortMap)
        chrMax, value = sortMap[0]
        print(str(chrMax)+' '+str(value))
        messageOut.append(chrMax)


    return "".join(messageOut)


def main():
    test1 = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar"
    ]
    test2 = []
    with open("input.txt", "r") as f:
        fdata = f.readlines()
        for line in fdata:
            seqIn = line.strip()
            test2.append(seqIn)


    testMatrix = []
    for seq1 in test2:
        testMatrix.append([chr1 for chr1 in seq1])

    #print(testMatrix)
    #message = repetitionCodeA(testMatrix)
    message = repetitionCodeB(testMatrix)
    print(message)

if __name__ == '__main__':
    main()
