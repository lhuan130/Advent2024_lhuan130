#GET DATA FROM FILE
f = open("input.txt", 'r')
data = f.readlines()
f.close()

print(len(data))
print()

#SOME HELPER VALUES


#PROBLEM 1
print("Problem 1")

totalVals = []
operVals = []
for line in data:
    lineData = line.split(':')
    totalVals.append(int(lineData[0]))
    operVals.append(list(map(int, (lineData[1].strip()).split(' '))))

#print(totalVals[0])
#print(operVals[0])

validSum = 0
for i in range(len(data)):
    #valid = False
    operation = 0
    while (operation < 2 ** len(operVals[i])):
        current = operVals[i][0]
        operatorCurrent = operation
        target = 1
        while current < totalVals[i]:
            if target == len(operVals[i]):
                break
            if (operatorCurrent % 2 == 0):
                current = current + operVals[i][target]
            else:
                current = current * operVals[i][target]
            operatorCurrent = operatorCurrent >> 1
            target = target + 1
        if current == totalVals[i]:
            validSum = validSum + totalVals[i]
            #valid = True
            #print(i, operation)
            break
        else:
            operation = operation + 1
    #if not valid:
        #print(i, "No valid operators found")

print(validSum)
print()

#PROBLEM 2
print("Problem 2")
import math
newSum = 0
for i in range(len(data)):
    operation = 0
    notvalid = True
    while operation < (3 ** (len(operVals[i]) - 1)):
        current = operVals[i][0]
        operatorCurrent = operation
        for x in operVals[i][1:]:
            if (operatorCurrent % 3 == 1):
                current = current + x
            elif (operatorCurrent % 3 == 2):
                current = current * x
            else:
                current = int(str(current)+str(x))
            operatorCurrent = math.floor(operatorCurrent / 3)
        if current == totalVals[i]:
            newSum = newSum + totalVals[i]
            notvalid = False
            print(i, operation)
            break
        else:
            operation = operation + 1
    if notvalid:
        print(i, "No valid operators found")

print(newSum)
