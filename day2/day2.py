#Adam Shechter
#Advent of code day 2

KEYPAD = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
class passCode(object):
    def __init__(self):
        self.location = {'row': 1, 'col': 1}

    def move(self, direction):
        if direction=='U':
            if self.location['row'] > 0:
                self.location['row'] -= 1
            else:
                pass
        elif direction=='D':
            if self.location['row'] < 2:
                self.location['row'] += 1
            else:
                pass
        elif direction=='L':
            if self.location['col'] > 0:
                self.location['col'] -= 1
            else:
                pass
        elif direction=='R':
            if self.location['col'] < 2:
                self.location['col'] += 1
            else:
                pass
KEYPAD_B = [
    [-1,  -1,  '1', -1,  -1],
    [-1,  '2', '3', '4', -1],
    ['5', '6', '7', '8', '9'],
    [-1,  'A', 'B', 'C', -1],
    [-1,  -1,  'D', -1,  -1]
]

class passCodeB(object):
    def __init__(self):
        self.location = {'row': 2, 'col': 0}

    def move(self, direction):
        if direction=='U':
            if self.location['row'] > 0:
                if KEYPAD_B[self.location['row'] - 1][self.location['col']] != -1:
                    self.location['row'] -= 1
            else:
                pass
        elif direction=='D':
            if self.location['row'] < 4:
                if KEYPAD_B[self.location['row'] + 1][self.location['col']] != -1:
                    self.location['row'] += 1
            else:
                pass
        elif direction=='L':
            if self.location['col'] > 0:
                if KEYPAD_B[self.location['row']][self.location['col'] - 1] != -1:
                    self.location['col'] -= 1
            else:
                pass
        elif direction=='R':
            if self.location['col'] < 4:
                if KEYPAD_B[self.location['row']][self.location['col'] + 1] != -1:
                    self.location['col'] += 1
            else:
                pass

def main():
    test1 = ['ULL',
            'RRDDD',
            'LURDL',
            'UUUUD']
    test2 = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            test2.append(line)

    finalCode = ''
    day2code1 = passCode()
    day2code2 = passCodeB()

    for cRow in test2:
        for cmd in cRow:
            #print(cmd)
            day2code2.move(cmd)
        currChar = KEYPAD_B[day2code2.location['row']][day2code2.location['col']]
        finalCode+= currChar
    return finalCode

if __name__ = '__main__':
    print(main())
