#Adam Shechter
#Advent of code day 9


def decompressTextA(compStr):
    bufferStr = ""
    outputStr = ""

    isCompressedText = False
    skipStep = {
        'isSkipStep': False,
        'endSkipIndex': 0
    }
    # might be more efficient to convert to while loop and set index to end of block.
    for index in range(len(compStr)):
        currChar = compStr[index:index+1]
        if currChar == '(' and not isCompressedText:
            #first paranthesis declaring a compressed text sequence
            isCompressedText = True
            indexEnd = index
            for j in range(index, len(compStr)):
                if compStr[j:j+1] == ')':
                    indexEnd = j
                    break
            rawInstr = compStr[index+1:indexEnd].split('x')
            print(rawInstr)
            blockSize = int(rawInstr[0])
            repetition = int(rawInstr[1])
            blockStr = compStr[indexEnd+1:indexEnd+1+blockSize]
            for rep in range(repetition):
                outputStr+=blockStr
            skipStep['isSkipStep'] = True
            skipStep['endSkipIndex'] = indexEnd+blockSize
        elif not isCompressedText:
            outputStr += currChar
        elif isCompressedText and skipStep['isSkipStep']:
            if index == skipStep['endSkipIndex']:
                skipStep['isSkipStep'] = False
                isCompressedText = False
    return outputStr


def decompressTextB(compStr):
    # recursive function
    outputLength = 0
    index = 0
    while index < len(compStr):
        currChar = compStr[index:index+1]
        print('currChar: '+currChar)
        if currChar == '(':
            indexEnd = index
            #first paranthesis declaring a compressed text sequence
            for j in range(index, len(compStr)):
                if compStr[j:j+1] == ')':
                    indexEnd = j
                    break
            rawInstr = compStr[index+1:indexEnd].split('x')
            print(rawInstr)
            blockSize = int(rawInstr[0])
            repetition = int(rawInstr[1])
            blockStr = compStr[indexEnd+1:indexEnd+1+blockSize]
            outputLength += (decompressTextB(blockStr) * repetition)
            index = indexEnd + blockSize
        else:
            outputLength += 1
        #iterator
        index+=1
    return outputLength

def main():
    test1 = [
    "ADVENT",
    "(3x3)XYZ",
    "X(8x2)(3x3)ABCY",
    "(27x12)(20x12)(13x14)(7x10)(1x12)A",
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
    ]
    test2 = ""

    with open("input.txt", "r") as f:
        fdata = f.readlines()
        data = fdata[0].strip()
        test2 = data

    # print("test2")
    # print(test2)
    # print("Length: "+str(len(test2)))
    # test1Decompressed = ""
    # for str1 in test1:
    #     print("IN: "+str1)
    #     test1Decompressed = decompressText(str1)
    #     print("OUT: "+test1Decompressed)
    #     print("Length: "+str(len(test1Decompressed)))

    # test1Decompressed = decompressTextA(test2)
    # print("OUT: "+test1Decompressed)
    # print("Length: "+str(len(test1Decompressed)))
    for str1 in test1:
        print("IN: "+str1)
        test1Decompressed = decompressTextB(str1)
        print("Length: "+str(test1Decompressed))
    test2DecompLength = 0
    test2DecompLength = decompressTextB(test2)
    print("VERSION 2 ")
    print("Length: "+str(test2DecompLength))

if __name__=="__main__":
    main()
