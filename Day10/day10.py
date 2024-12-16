f = open("input.txt", 'r')
topMap = f.readlines()
f.close()
for i in range(len(topMap)):
    topMap[i] = list(map(int, list(topMap[i].strip())))
print(topMap)

#PROBLEM 1

def findTrail(data, row, col, nextElev, elevList):
    if data[row][col] != nextElev:
        return
    if data[row][col] == 9:
        for i in range(len(elevList)):
            if row == elevList[i][0] and col == elevList[i][1]:
                return
        elevList.append((row, col))
        return
    score = 0
    if (row > 0):
        #test above
        findTrail(data, (row - 1), col, (nextElev + 1), elevList)
    if (row < len(data) - 1):
        #test below
        findTrail(data, (row + 1), col, (nextElev + 1), elevList)
    if (col < len(data[row]) - 1):
        #test right
        findTrail(data, row, (col + 1), (nextElev + 1), elevList)
    if (col > 0):
        #test left
        findTrail(data, row, (col - 1), (nextElev + 1), elevList)

score = 0
for i in range(len(topMap)):
    for j in range(len(topMap[i])):
        if (topMap[i][j] == 0):
            reached = []
            findTrail(topMap, i, j, 0, reached)
            score += len(reached)

print()
print("PROBLEM 1")
print(score)

#PROBLEM 2

def findRate(data, row, col, nextElev):
    if data[row][col] != nextElev:
        return 0
    if data[row][col] == 9:
        return 1
    rating = 0
    if (row > 0):
        #test above
        rating += findRate(data, (row - 1), col, (nextElev + 1))
    if (row < len(data) - 1):
        #test below
        rating += findRate(data, (row + 1), col, (nextElev + 1))
    if (col < len(data[row]) - 1):
        #test right
        rating += findRate(data, row, (col + 1), (nextElev + 1))
    if (col > 0):
        #test left
        rating += findRate(data, row, (col - 1), (nextElev + 1))
    return rating

ratingSum = 0
for i in range(len(topMap)):
    for j in range(len(topMap[i])):
        ratingSum += findRate(topMap, i, j, 0)
print(ratingSum)
print("PROBLEM 2")
print()
