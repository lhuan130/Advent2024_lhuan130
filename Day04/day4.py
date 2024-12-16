f = open("input.txt", 'r')
data = f.readlines()
f.close()

def checkX(inData, row, col):
    ret = 0
    checkUp = False
    checkLeft = False
    checkDown = False
    checkRight = False
    if (row > 2):
        checkUp = True
    if (row < len(inData) - 3):
        checkDown = True
    if (col < len(inData[0]) - 3):
        checkRight = True
    if (col > 2):
        checkLeft = True
    
    if checkUp:
        if inData[row - 1][col] == 'M' and inData[row - 2][col] == 'A' and inData[row - 3][col] == 'S':
            ret += 1
        if checkLeft:
            if inData[row - 1][col - 1] == 'M' and inData[row - 2][col - 2] == 'A' and inData[row - 3][col - 3] == 'S':
                ret += 1
        if checkRight:
            if inData[row - 1][col + 1] == 'M' and inData[row - 2][col + 2] == 'A' and inData[row - 3][col + 3] == 'S':
                ret += 1
    if checkDown:
        if inData[row + 1][col] == 'M' and inData[row + 2][col] == 'A' and inData[row + 3][col] == 'S':
            ret += 1
        if checkLeft:
            if inData[row + 1][col - 1] == 'M' and inData[row + 2][col - 2] == 'A' and inData[row + 3][col - 3] == 'S':
                ret += 1
        if checkRight:
            if inData[row + 1][col + 1] == 'M' and inData[row + 2][col + 2] == 'A' and inData[row + 3][col + 3] == 'S':
                ret += 1
    if checkRight:
        if inData[row][col + 1] == 'M' and inData[row][col + 2] == 'A' and inData[row][col + 3] == 'S':
            ret += 1
    if checkLeft:
        if inData[row][col - 1] == 'M' and inData[row][col - 2] == 'A' and inData[row][col - 3] == 'S':
            ret += 1
    return ret

def checkMas(inData, row, col):
    topLeft = inData[row - 1][col - 1]
    bottomLeft = inData[row + 1][col - 1]
    topRight = inData[row - 1][col + 1]
    bottomRight = inData[row + 1][col + 1]
    if (topLeft == bottomRight):
        return 0
    if (topRight == bottomLeft):
        return 0
    if not(topLeft == 'M' or topLeft == 'S'):
        return 0
    if not(bottomLeft == 'M' or bottomLeft == 'S'):
        return 0
    if not(bottomRight == 'M' or bottomRight == 'S'):
        return 0
    if not(topRight == 'M' or topRight == 'S'):
        return 0
    return 1


count = 0
count2 = 0
#check verticles on every X
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == 'X':
            count += checkX(data, i, j)
        if i > 0 and i < len(data) - 1 and j > 0 and j < len(data[i]) - 1 and data[i][j] == 'A':
            count2 += checkMas(data, i, j)

print("Problem 1")
print(count)

print("Problem 2")
print(count2)
