#Adam Shechter
#Advent of code day 7


def validateTLS(ipStr):

    isOutsideBlock = True
    ValidOutsideBlock = False
    InvalidInsideBlock = False

    for i, currChar in enumerate(ipStr):
        #print(i)
        #print(currChar)
        if currChar == '[':
            isOutsideBlock = False
            continue
        elif currChar == ']':
            isOutsideBlock = True
            continue

        if i == (len(ipStr)-3):
            break
        # ABBA pattern search
        if ipStr[i:i+1] == ipStr[i+3:i+4] and ipStr[i+1:i+2] == ipStr[i+2:i+3]:
            if ipStr[i:i+1] != ipStr[i+1:i+2]:
                if isOutsideBlock:
                    #Inside blcok validates IP
                    ValidOutsideBlock = True
                else:
                    #Inside block invalidated IP
                    InvalidInsideBlock = True
                    return False

    if ValidOutsideBlock:
        return True
    else:
        return False

def validateSSL(ipStr):

    isOutsideBlock = True
    outsideBlocksTest = []
    insideBlocksTest = []

    for i, currChar in enumerate(ipStr):
        #print(i)
        #print(currChar)
        if currChar == '[':
            isOutsideBlock = False
            continue
        elif currChar == ']':
            isOutsideBlock = True
            continue

        if i == (len(ipStr)-2):
            break
        # ABBA pattern search
        if ipStr[i:i+1] == ipStr[i+2:i+3]:
            if ipStr[i:i+1] != ipStr[i+1:i+2] and ipStr[i+1:i+2] not in ['[',']']:
                if isOutsideBlock:
                    #Inside block validates IP
                    outsideBlocksTest.append(ipStr[i:i+3])
                else:
                    #Inside block invalidated IP
                    insideBlocksTest.append(ipStr[i:i+3])

    #print("outsideBlocksTest")
    #print(outsideBlocksTest)
    #print("insideBlocksTest")
    #print(insideBlocksTest)


    for outsidePattern in outsideBlocksTest:
        for insidePattern in insideBlocksTest:
            if outsidePattern[0:1] == insidePattern[1:2] and outsidePattern[1:2] == insidePattern[0:1]:
                return True

    return False

def main():
    test1 = [
    "aba[bab]xyz",
    "xyx[xyx]xyx",
    "aaa[kek]eke",
    "zazbz[bzb]cdb",
    "rhamaeovmbheijj[hkwbkqzlcscwjkyjulk]ajsxfuemamuqcjccbc",
    "gdlrknrmexvaypu[crqappbbcaplkkzb]vhvkjyadjsryysvj[nbvypeadikilcwg]jwxlimrgakadpxu[dgoanojvdvwfabtt]yqsalmulblolkgsheo",
    "byddropvzudnjciymyh[jcebyxyvikkshpn]ggmrxgkzsrfkfkzo"
    ]
    test2 = []
    with open("input.txt", "r") as f:
        fdata = f.readlines()
        for line in fdata:
            data = line.strip()
            test2.append(data)

    validTlsCount = 0
    validSSLCount = 0
    for ipStr in test2:
        isValidTLS = False
        isValidSSL = False
        isValidTLS = validateTLS(ipStr)
        print('IP: '+ipStr)
        print("TLS valid: "+str(isValidTLS))
        if isValidTLS:
            validTlsCount+=1
        isValidSSL = validateSSL(ipStr)
        print("SSL valid: "+str(isValidSSL))
        if isValidSSL:
            validSSLCount+=1


    print("valid TLS ip's: "+str(validTlsCount))
    print("valid SSL ip's: "+str(validSSLCount))

if __name__=='__main__':
    main()
