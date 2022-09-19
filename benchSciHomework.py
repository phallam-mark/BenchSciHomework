from itertools import combinations

def numberFinder(inputStr):

    inputCharList = []
    intList = []
    count = 0
    notCount = 0
    comboList = list()

    # convert the input string into a list of characters
    for letter in inputStr:
        inputCharList.append(letter)

    # for each of the characters in the list, map the char to an int
    # and add that int to a list of ints
    for char in inputCharList:
        if char == 'a' or char == 'b':
            intList.append(1)
        elif char == 'c' or char == 'd' or char == 'e':
            intList.append(2)
        elif char == 'f' or char == 'g' or char == 'h':
            intList.append(3)
        elif char == 'i' or char == 'j' or char == 'k':
            intList.append(4)
        elif char == 'l' or char == 'm' or char == 'n':
            intList.append(5)
        elif char == 'o' or char == 'p' or char == 'q':
            intList.append(6)
        elif char == 'r' or char == 's' or char == 't':
            intList.append(7)
        elif char == 'u' or char == 'v' or char == 'w':
            intList.append(8)
        else: 
            intList.append(9)
    
    # create a list consisting of all of the possible combinations of the mapped integers
    for num in range (len(intList) + 1):
        comboList += list(combinations(intList, num))

    # for each of the possible combinations of integers, if the of sum of the integers
    # is evenly divisible by the count of the integers, increment the count
    for combo in comboList:
        if not combo:
            notCount = notCount + 1
        else:
            if sum(combo) % len(combo) == 0:
                count = count + 1

    return count


inputStr = input("Enter a string of chars: ")
count = numberFinder(inputStr)

print("count =  ", count)
