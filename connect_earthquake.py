__author__ = 'Ota'
import random
import sys

slot = []
NumSlot = [0, 0,  0, 0, 0, 0, 0]

def check_vertical(x, y, sign):
    point = []
    for ind in range(0, 4):
        if y-ind >= 0:
            s = slot[x][y-ind]
            if s == sign:
                point.append(3)
            elif s == " ":
                point.append(0.3)
            else:
                point.append(0)
        else:
            point.append(0.3)
        '''point_return *= point[ind]'''
    return point

def check(n, x, y, sign):
    point = []

    for ind in range(0, 4):
        sx = x+ind-n
        sy = y+ind-n
        if sy >= 0:
            s = slot[x+ind-n][y+ind-n]
            if s == sign:
                point.append(3)
            elif s == " ":
                point.append(0.3)
            else:
                point.append(0)
        else:
            point.append(0)
        '''point_return *= point[ind]'''

    for ind in range(0, 4):
        if y-ind+n >= 0:
            s = slot[x+ind-n][y-ind+n]
            if s == sign:
                point.append(3)
            elif s == " ":
                point.append(0.3)
            else:
                point.append(0)
        else:
            point.append(0)
        '''point_return *= point[ind]'''

    for ind in range(0, 4):
        s = slot[x+ind-n][y]
        if s == sign:
            point.append(3)
        elif s == " ":
            point.append(0.3)
        else:
            point.append(0)
        '''point_return *= point[ind]'''

    return point

def caliculate_point(res):
    a = res[0]*res[1]*res[2]*res[3]
    b = res[4]*res[5]*res[6]*res[7]
    c = res[8]*res[9]*res[10]*res[11]
    result_cal = a + b + c
    '''result = []
    result.append(a)
    result.append(b)
    result.append(c)
    '''
    return result_cal

def terminal_test(x, y, sign):
    res = check_vertical(x, y, sign)
    a = res[0]*res[1]*res[2]*res[3]
    print "vertical point = "
    print a

    if x == 0:
        res = check(0, x, y, sign)
        answer = caliculate_point(res)
    elif x == 1:
        res = check(0, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer2 = caliculate_point(res)
        answer = answer1+answer2
    elif x == 2:
        res = check(0, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer1+answer2 + answer3
    elif x == 3:
        res = check(0, x, y, sign)
        answer0 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer0+answer1+answer2+answer3
    elif x == 4:
        res = check(1, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer1+answer2+answer3
    elif x == 5:
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer2+answer3
    elif x == 6:
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer3

    print answer
    if answer + a >81:
        return True
    else:
        return False

def earthquake():
    die = random.randint(0, 3)
    if die == 1:
        print ("earthquake happens ")
        for i in range(7):
            for j in range(9):
                slot[i][j] = slot[i][j + 1]
                if NumSlot[i] <= 0:
                    NumSlot[i] = 0
                else:
                    NumSlot[i] -= 1
                """ if j == 9:
                    slot[i][j] = " " """
    else:
        """Nothing will happen """
        pass




SlotX = 0


for i in range(8):
    slot.append([])

for i in range(8):
    for j in range(10):
        slot[i].append(" ")


done = False

firstFlag = raw_input("would like to go first (y/n)")
print (firstFlag)


earthquakeFlag = raw_input("Should I tell you when earthquake happen (y/n)")
print (earthquakeFlag)

while done is False:
    SlotX = input("Please enter a slot from 1 to 7 for your move")
    print SlotX
    SlotX -= 1
    if SlotX in range(0, 7):

        if firstFlag != "y":
            playSlotX = random.randint(0, 6)
            playSlotY = NumSlot[playSlotX]
            slot[playSlotX][playSlotY] = "o"
            NumSlot[playSlotX] += 1
            SlotY = NumSlot[SlotX]
            slot[SlotX][SlotY] = "x"
            NumSlot[SlotX] += 1
        else:
            SlotY = NumSlot[SlotX]
            slot[SlotX][SlotY] = "x"
            NumSlot[SlotX] += 1
            playSlotX = random.randint(0, 6)
            playSlotY = NumSlot[playSlotX]
            slot[playSlotX][playSlotY] = "o"
            NumSlot[playSlotX] += 1


        for i in range(10):
            for j in range(7):
                sys.stdout.write("|")
                if i <= NumSlot[j]:
                    sys.stdout.write(slot[j][i])
                else:
                    sys.stdout.write(" ")

            sys.stdout.write("|")
            print " "
        done = terminal_test(SlotX, SlotY, "x")

        if earthquakeFlag == "y":
            earthquake()


print "Finished"




