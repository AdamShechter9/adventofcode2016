#Adam Shechter
#Advent of code day 5

# running an md5 checksum
# secret puzzle input is 'reyedfim'

import hashlib

PUZZLEINPUT = 'reyedfim'

#print (hashlib.algorithms_guaranteed)
#
# testStr = "abc3231929"
# md5 = hashlib.md5(testStr.encode("utf-8"))
# print(md5.hexdigest())
#
# testStr = "abc5017308"
# md5 = hashlib.md5(testStr.encode("utf-8"))
# print(md5.hexdigest())
#
# testStr = "abc5278568"
# md5 = hashlib.md5(testStr.encode("utf-8"))
# print(md5.hexdigest())

def main():
    password = [-1,-1,-1,-1,-1,-1,-1,-1]
    counter = 0
    while -1 in password:
        testStr = PUZZLEINPUT+str(counter)
        md5 = hashlib.md5(testStr.encode("utf-8"))
        hashTest = str(md5.hexdigest())
        #print(testStr+"   ->   "+hashTest)
        if hashTest[:5] == '00000':
            try:
                index = int(hashTest[5:6])
                if index < 8 and password[index] == -1:
                    password[index]= hashTest[6:7]
                    strPassword = [str(chr1) for chr1 in password]
                    print("\n\ncurrent password: "+"".join(strPassword))
            except ValueError:
                pass
        counter += 1
    return "".join(password)

if __name__ == '__main__':
    print(main())
