#Adam Shechter
#Advent of code day 4

# running a "checksum" validation on strings
'''
Rules
    hash(string)-SECTORID(INT)[checksum]

hash-
    1. five most popular letters
    2. letters are in order of popularity
    3. ties are decided by alphabetization


aaaaa-bbb-z-y-x-123[abxyz]
is a real room because the most common letters are a (5), b (3),
and then a tie between x, y, and z, which are listed alphabetically.

a-b-c-d-e-f-g-h-987[abcde]
is a real room because although the letters are all tied (1 of each),
the first five are listed alphabetically.

not-a-real-room-404[oarel]
is a real room.

totally-real-room-200[decoy]
is not.
'''

def validateRoom(hashTest):
    chrMap = {}
    checksum = hashTest[-6:-1]
    sectorId = hashTest[-10:-7]
    nameRaw = hashTest[:-10].strip('-').split('-')
    name = "".join(nameRaw)
    #print("Encrypted Room Name: "+name)
    #print("sector id: "+sectorId)
    #print("room checksum: "+checksum)

    for currChar in name:
        try:
            chrMap[currChar] += 1
        except KeyError:
            chrMap[currChar] = 1

    freqMap = sorted(chrMap.items(), key=lambda x: x[1], reverse=True)
    sortList = []
    currBlock = ""
    for i in range(len(freqMap)):
        chr1, freq1 = freqMap[i]
        if i < (len(freqMap) - 1):
            chr2, freq2 = freqMap[i+1]
        else:
            #Last element on the list add to last bucket.
            freq2 = freq2 - 1
        currBlock+=chr1
        if freq1 > freq2:
            sortList.append(currBlock)
            currBlock = ""
        elif freq1 == freq2:
            pass

    for j in range(len(sortList)):
        temp = [x for x in sortList[j]]
        temp2 = sorted(temp)
        sortList[j] = "".join(temp2)
    checksumResult = "".join(sortList)[:5]
    #print("checksum check: "+str(checksumResult))
    return checksumResult == checksum, sectorId

def decryptRoom(cipherHash):
    sectorId = int(cipherHash[-10:-7])
    nameRaw = cipherHash[:-10].strip('-').split('-')
    #print("Encrypted Room Name: "+str(nameRaw))
    #print("sector id: "+str(sectorId))
    decipherNameA = []
    for block in nameRaw:
        blockTxt = ""
        for currChar in block:
            currOrd = ord(currChar) - 97
            currOrd = (currOrd + (sectorId % 26)) % 26
            mChar = chr(currOrd+97)
            blockTxt+=mChar
        decipherNameA.append(blockTxt)
    decipherName = " ".join(decipherNameA)
    return decipherName+" "+str(sectorId)

def mainA():
    test1 = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]
    test2 = []
    with open('input.txt', 'r') as f:
        fdata = f.readlines()
        for lines in fdata:
            data = lines.strip()
            test2.append(data)
    validRooms = 0
    sectorIdSum = 0
    with open('validrooms.txt', 'w') as f:
        for roomHash in test2:
            valid, sectId = validateRoom(roomHash)
            #print(valid)
            if valid:
                validRooms += 1
                f.write(roomHash+'\n')
                sectorIdSum+=int(sectId)
    return validRooms, len(test2), sectorIdSum

def mainB():
        test2 = []
        with open('validrooms.txt', 'r') as f:
            fdata = f.readlines()
            for lines in fdata:
                data = lines.strip()
                test2.append(data)
        with open('roomsdecrypted.txt', 'w') as f:
            for roomHash in test2:
                decryptTxt = decryptRoom(roomHash)
                print(decryptTxt)
                f.write(decryptTxt+'\n')
        return True

if __name__ == '__main__':
    #sumValidRooms, totalRooms, sectorIdSum = mainA()
    #print("Sum of real rooms: "+str(sumValidRooms)+" / "+str(totalRooms))
    #print("Sum of sector IDs: "+str(sectorIdSum))
    mainB()
