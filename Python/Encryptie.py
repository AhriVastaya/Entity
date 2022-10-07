from re import I
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

#Splitting the InputString into a list that contains either the elements with an even or odd index.
#Initialize Lists for the split list.
EvenChars = []
OddChars = []
Index = 0
#Sorting every element based on it's index.
for i in InputString:
    #Check if the index of the element is even by cheching the remainder when euclidly dividing by 2.
    if Index % 2 ==0:
        #Add it to the list of elements with even indexes.
        EvenChars.append(i)
    #If the remainder is 1, the index is odd.
    else:
        #Add it to the list of elements with odd indexes.
        OddChars.append(i)
    #Increment the index by one to move on to the next element.
    Index += 1

#Manipulate the characters from the list containing the elements with even indexes by applying a Caesar-encryption to them.
Index = 0
for i in EvenChars:
    #If the element is an integer, there are only 10 possibilities.
    if GetType(i) == 1:
        #ord(0) = 48, so I subtract it by 48 to make the modulus calculation work.
        _ord = ord(i) - 48
        #Shift the ASCII code of the element by the amount defined by the user.
        _ord += ShiftValue
        #Take the modulo of 10 to make sure that _ord has a value between 0 and 10.
        _ord = _ord % 10
        #Add the 48 back in.
        _ord = _ord + 48
    elif GetType(i) == 3:
        _ord = ord(i) - 97
        _ord += ShiftValue
        _ord = _ord % 26
        _ord = _ord + 97
    i = chr(_ord)
    EvenChars[Index] = i
    Index += 1
