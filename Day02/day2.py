f = open("input2.txt")
lines = f.readlines()
f.close()

safe = 0
actualSafe = 0

for line in lines:
    isSafe = True
    data = list(map(int, line.split(' ')))
    i = -1
    while i < (len(data) - 3):
        i = i + 1
        diff1 = data[i + 1] - data[i]
        diff2 = data[i + 2] - data[i + 1]
        diff3 = data[i + 2] - data[i]
        if (abs(diff1) > 3) or (abs(diff2) > 3):
            isSafe = False
        if (diff1 == 0) or (diff2 == 0):
            isSafe = False
        #diff check
        if (diff1 > 0) and (diff2 < 0):
            isSafe = False
        elif (diff1 < 0) and (diff2 > 0):
            isSafe = False
    #check last pair
    i = i + 1
    diff = data[i + 1] - data[i]
    if (diff == 0) or (abs(diff) > 3):
        isSafe = False
    if isSafe:
        safe = safe + 1
        actualSafe = actualSafe + 1
    else:
        safeFound = False
        i = -1
        while i < len(data) - 1:
            i = i + 1
            #remove
            removedVal = data.pop(i)
            #print(removedVal)
            isSafe = True
            j = -1
            while j < len(data) - 3:
                j = j + 1
                diff1 = data[j + 1] - data[j]
                diff2 = data[j + 2] - data[j + 1]
                if (abs(diff1) > 3) or (abs(diff2) > 3):
                    isSafe = False
                if (diff1 == 0) or (diff2 == 0):
                    isSafe = False
                if (diff1 > 0) and (diff2 < 0):
                    isSafe = False
                if (diff1 < 0) and (diff2 > 0):
                    isSafe = False
            j = j + 1
            diff = data[j + 1] - data[j]
            if (diff == 0) or (abs(diff) > 3):
                isSafe = False
            if isSafe:
                safeFound = True
            #replace
            data[i:i] = [removedVal]
            if safeFound:
                actualSafe = actualSafe + 1
                #print("dampenered")
                break

print("Problem 1")
print(safe)

print("Problem 2")
print(actualSafe)
