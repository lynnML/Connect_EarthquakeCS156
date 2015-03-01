import random
import sys
"""
firstFlag = input("would like to go first (y/n)")
print (firstFlag)
earthquakeFlag = input("Should I tell you when earthquake happen (y/n)")
print (earthquakeFlag)
"""

slotNo = 0

slot=[]
for i in range(8):
   slot.append([])

for i in range(8):
   slot[i].append("x")


slotNum=[0,0,0,0,0,0,0]
while(slotNo!=9):
   slotNo = input("Please enter a slot from 1 to 7 for your move")
   print slotNo
   slotNo=slotNo-1
   if (slotNo>=0 and slotNo<=7):
       slotNum[slotNo]=slotNum[slotNo]+1
       slot[slotNo].append("x")
       playSlot=random.randint(0,6)
       slotNum[playSlot]=slotNum[playSlot]+1
       slot[playSlot].append("o")
       for i in range(10):
           for j in range(7):
               sys.stdout.write("|")
               if (i<=slotNum[j]):
                   sys.stdout.write(slot[j][i])
               else:
                   sys.stdout.write(" ")

           sys.stdout.write("|")
           print " "



def isComplete():
