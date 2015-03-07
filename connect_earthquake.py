__author__ = 'Kaya'
import random
import sys

slot = []
done = False
rowCounter = 0
column_height = [0, 0,
                 0, 0,
                 0 ,0,
                 0]

NumSlot = [0, 
           0,
           0, 
           0,
           0, 
           0,
           0]



def check_vertical(x, y, sign):
    point = []
    for ind in range(0, 4):
        if y - ind >= 0:
            s = slot[x][y - ind]
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
        sx = x + ind - n
        sy = y + ind - n
        if sy >= 0:
            s = slot[x + ind - n][y + ind - n]
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
        if y - ind + n >= 0:
            s = slot[x + ind - n][y - ind + n]
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
        s = slot[x + ind - n][y]
        if s == sign:
            point.append(3)
        elif s == " ":
            point.append(0.3)
        else:
            point.append(0)
        '''point_return *= point[ind]'''

    return point


def caliculate_point(res):
    a = res[0] * res[1] * res[2] * res[3]
    b = res[4] * res[5] * res[6] * res[7]
    c = res[8] * res[9] * res[10] * res[11]
    result_cal = a + b + c
    '''result = []
    result.append(a)
    result.append(b)
    result.append(c)
    '''
    return result_cal


def utility(x, y, sign):
    global answer
    if x == 0:
        res = check(0, x, y, sign)
        answer = caliculate_point(res)
    elif x == 1:
        res = check(0, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer2 = caliculate_point(res)
        answer = answer1 + answer2
    elif x == 2:
        res = check(0, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer1 + answer2 + answer3
    elif x == 3:
        res = check(0, x, y, sign)
        answer0 = caliculate_point(res)
        res = check(1, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer0 + answer1 + answer2 + answer3
    elif x == 4:
        res = check(1, x, y, sign)
        answer1 = caliculate_point(res)
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer1 + answer2 + answer3
    elif x == 5:
        res = check(2, x, y, sign)
        answer2 = caliculate_point(res)
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer2 + answer3
    elif x == 6:
        res = check(3, x, y, sign)
        answer3 = caliculate_point(res)
        answer = answer3

    print (answer)
    return answer


def terminal_test(x, y, sign):
    res = check_vertical(x, y, sign)
    a = res[0] * res[1] * res[2] * res[3]

    answer = utility(x, y, sign)

    if answer + a > 81:
        return True
    else:
        return False


def ai_action():
    score_ai = []
    score_human = []
    score_total = []
    max_index = 0
    for ip in range(0, 7):
        ai_result = utility(ip, NumSlot[ip], "o")
        human_result = utility(ip, NumSlot[ip], "x")
        score_ai.append(ai_result)
        score_human.append(human_result)
        score_total.append(ai_result + human_result)
    max_val = score_ai[0]
    for index in range(0, 7):
        if max_val <= score_ai[index]:
            max_val = score_ai[index]
            max_index = index
        else:
            pass
    print ("max_index = ", max_index + 1)

    return max_index

'''
def print_slot():
    print ("|1|2|3|4|5|6|7|")
    for i in range(10):
        for j in range(7):
            sys.stdout.write("|")
            if i <= NumSlot[j]:
                sys.stdout.write(slot[j][i])
            else:
                sys.stdout.write(" ")

        sys.stdout.write("|")
        print " "
'''
def print_slot():
    global slot
    global numSlot
    global rowCounter
    list = []
    
    for row in range(rowCounter):
        
        p ="|"
        for col in range(7):
            if slot[row][col] == "x"  or slot[row][col] == "o":
                p += slot[row][col]
                p += "|"
            else:
                p += " |"

        list.append(p)
    x = rowCounter
    
    while(x > 0):
        print(list[x - 1])
        x -= 1
    print "|1|2|3|4|5|6|7|"
         

def earthquake():
    die = random.randint(0, 6)
    if die == 1:
        print ("earthquake happens ")
        for ei in range(7):
            for ej in range(9):
                slot[ei][ej] = slot[ei][ej + 1]

            if NumSlot[ei] <= 0:
                NumSlot[ei] = 0
            else:
                NumSlot[ei] -= 1
            """ if j == 9:
                slot[i][j] = " " """
    else:
        """Nothing will happen """
        pass
    
    
def whichWin(human_done, ai_done):
    """Return true if human wins, otherwise false"""
    if human_done is True:
        SlotX = 0
   
def promptCheck(UserSelection):
    
    if(UserSelection == 'y' or UserSelection == 'n'):
        return 0
    else:
        print "Invalid Selection.\n Please type 'y' for YES or 'n' for NO.\n"


def addRow():
    
    global rowCounter
    global slot
    
    slot.append([])
    i = len(slot)
    for j in range(7):
        slot[rowCounter].append(" ")
       

def check_ifRowNeeded():
    global rowCounter
    global column_height
    for ch in column_height:
        if(ch > rowCounter):
            addRow()
            rowCounter += 1
    


def col_height(addToColumn):
    global column_height
    column_height[addToColumn - 1] += 1
    #print "this is Column_height: ", column_height

# Temporary Build of Board
def build():
    global slot
    global rowCounter
    rowCounter = 10
    
    for i in range(rowCounter):
        slot.append([])
        for j in range(7):
            slot[i].append(" ")            
            
         
###############Main#############






# Prompts Users If he/she goes first
while(True):
    firstFlag = raw_input("Would like to go first? [y/n]: ")
    #print (firstFlag)
    if(promptCheck(firstFlag) == 0):
        break

# Prompts User to inform about earthquake after every turn
while(True):    
    earthquakeFlag = raw_input("Should I tell you when earthquake happen? [y/n]: ")
    #print (earthquakeFlag)
    if(promptCheck(earthquakeFlag) == 0):
        break
    





while done is False:
    if firstFlag != "y":
        
    #playSlotX = random.randint(0, 6)
        playSlotX = ai_action()
        col_height(playSlotX + 1)
        check_ifRowNeeded()
        playSlotY = NumSlot[playSlotX]
        slot[playSlotX][playSlotY] = "o"
        NumSlot[playSlotX] += 1
        print_slot()
        SlotX = input("Please enter a slot from 1 to 7 for your move")
        print (SlotX)
        col_height(SlotX)
        check_ifRowNeeded()
        SlotX -= 1
        if SlotX in range(0, 7):
            SlotY = NumSlot[SlotX]
            slot[SlotX][SlotY] = "x"
            NumSlot[SlotX] += 1
    else:
        SlotX = input("Please enter a slot from 1 to 7 for your move")
        print SlotX
        col_height(SlotX)
        check_ifRowNeeded()
        print(slot)
        print(column_height)
        print(rowCounter)
        
        SlotX -= 1
        if SlotX in range(0, 6):
            #human's tern
            SlotY = NumSlot[SlotX]
            slot[SlotX][SlotY] = "x"
            NumSlot[SlotX] += 1
          
        #playSlotX = random.randint(0, 6)
            print_slot()
            human_done1 = terminal_test(SlotY, SlotX, "x")
 
            #checkWin1 = human_done or ai_done
 
            #Ai's tern
            print "before ai_action"
            print_slot()
            playSlotX = ai_action()
            col_height(playSlotX + 1)
            check_ifRowNeeded()
            print "after action"
            playSlotY = NumSlot[playSlotX]
            slot[playSlotX][playSlotY] = "o"
            NumSlot[playSlotX] += 1
            print_slot()
    human_done = terminal_test(SlotX, SlotY, "x")
    ai_done = terminal_test(playSlotX, playSlotY, "o")
 
    done = human_done or ai_done
    if earthquakeFlag == "y":
        earthquake()
        print_slot()
    if human_done is True:
        print "Human wins!!!"
    elif ai_done is True:
        print "AI wins!!"
    else:
        print "Keep Going!"

print "Finished"

