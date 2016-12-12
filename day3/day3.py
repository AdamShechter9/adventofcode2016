#Adam Shechter
#Advent of code day 3


def isTriangle(a,b,c):
    # tests for a+b>c a+c>b b+c>a
    validSet = 0
    if (a+b) > c and (a+c) > b and (b+c) > a:
        validSet = 1
    if validSet == 1:
        return True
    else:
        return False


def mainA():
    print("row makes triangles")
    validSet = 0
    count = 0
    with open('input.txt', 'r') as f:
        fdata = f.readlines()
        for lines in fdata:
            data = lines.strip()
            a,b,c = data.split()
            a,b,c = int(a), int(b), int(c)
            if isTriangle(a,b,c):
                validSet+=1
            count+=1

    print ("triangle count is: "+str(count))
    print ("valid sets: "+str(validSet))
    return validSet

def mainB():
    print("cols of 3 make triangles")
    validSet = 0
    count = 0
    with open('input.txt', 'r') as f:
        fdata = f.readlines()
        length = len(fdata)

        for i in range(length/3):
            index = i * 3
            a1,a2,a3 = fdata[index].split()
            b1,b2,b3 = fdata[index+1].split()
            c1,c2,c3 = fdata[index+2].split()
            a1,b1,c1 = int(a1),int(b1),int(c1)
            a2,b2,c2 = int(a2),int(b2),int(c2)
            a3,b3,c3 = int(a3),int(b3),int(c3)
            if isTriangle(a1,b1,c1):
                validSet+=1
            if isTriangle(a2,b2,c2):
                validSet+=1
            if isTriangle(a3,b3,c3):
                validSet+=1
            count+=3

    print ("triangle count is: "+str(count))
    print ("valid sets: "+str(validSet))
    return validSet

if __name__=='__main__'
    #print(mainA())
    print(mainB())
