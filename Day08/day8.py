#GET DATA FROM FILE
f = open("input.txt", 'r')
data = f.readlines()
f.close()

#preprocessing and setup
typeList = dict()
for i in range(len(data)):
    print(data[i].strip())
    data[i] = list(data[i].strip())
    for j in range(len(data[i])):
        if (data[i][j] != '.'):
            #add all unique antenna types to typeList
            inList = typeList.get(data[i][j])
            if inList == None:
                inList = []
            inList.append([i, j])
            typeList[data[i][j]] = inList
print(typeList)
        
antinodeMap = [[0 for j in range(len(data[0]))] for i in range(len(data))]

for uniqueFreq in typeList.keys():
    antennaList = typeList[uniqueFreq]
    if len(antennaList) < 2:
        continue
    for i in range(len(antennaList)):
        for j in range(i + 1, len(antennaList)):
            #print(antennaList[i], antennaList[j])
            #i and j are indices of two antenna of the same frequency
            antinodeMap[antennaList[i][0]][antennaList[i][1]] += 1#comment out for PROBLEM 1
            antinodeMap[antennaList[j][0]][antennaList[j][1]] += 1#comment out for PROBLEM 1
            distRat = 0
            f1 = True
            f2 = True
            while f1 or f2:
                distRat += 1
                f1 = False
                f2 = False
                nx1 = ((distRat + 1) * antennaList[i][0]) - (distRat * antennaList[j][0])
                nx2 = ((distRat + 1) * antennaList[j][0]) - (distRat * antennaList[i][0])
                ny1 = ((distRat + 1) * antennaList[i][1]) - (distRat * antennaList[j][1])
                ny2 = ((distRat + 1) * antennaList[j][1]) - (distRat * antennaList[i][1])
                #print(nx1, ny1, " ", nx2, ny2)
                if nx1 >= 0 and nx1 < len(data) and ny1 >= 0 and ny1 < len(data[0]):
                    antinodeMap[nx1][ny1] += 1
                    f1 = True
                if nx2 >= 0 and nx2 < len(data) and ny2 >= 0 and ny2 < len(data[0]):
                    antinodeMap[nx2][ny2] += 1
                    f2 = True
                #break
                #For PROBLEM 1, use this to break the while immediately after it is used because you only check once

uniqueAnt = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if antinodeMap[i][j] > 0:
            uniqueAnt += 1

print(uniqueAnt)
print()
