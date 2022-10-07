from textwrap import indent
from typing import Type

# Define a method to check a variable for its type.
def GetType(val):
    #Try all possible type and return a number based on the result (1 = int; 2 = float; 3 = string).
    #Also catch all errors to make sure the runtime doesn't get interrupted.
    try:
        int(val)
        return 1
    except ValueError: pass
    try:
        float(val)
        return 2
    except ValueError: pass
    try:
        str(val)
        return 3
    except ValueError: pass

#Get some input from the user.
InputString = input("Input: \n")
ShiftValue = input("Shift: \n")
#Repeat asking until he gives us an integer.
while GetType(ShiftValue) != 1:
    ShiftValue = input("Provide a valid Shift value: \n")
ShiftValue = int(ShiftValue)

#Split the InputString in a list containing the elements with an even and uneven index.
#Initialize Lists for the split list.
EvenChars = []
UnevenChars = []

for i in InputString:
    if InputString.index(i) % 2 ==0:
        EvenChars.append(i)
    else:
        UnevenChars.append(i)

#Manipulate the characters from the list containing the elements with even indexes by applying a Caesar-encryption to them.
for i in EvenChars:
    if GetType(i) == 1:
        break
    else: 
        break
    break