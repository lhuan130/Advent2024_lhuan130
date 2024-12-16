f = open("input.txt", 'r')
data = f.readlines()
f.close()

#all lines with (i < midPoint) are rules
#all lines with (i > midPoint) are page blocks
midPoint = 0
for i in range(len(data)):
    if data[i] == '\n':
        midPoint = i
        break

#list of rules, each stored as integer pair
ruleList = []
for i in range(midPoint):
    ruleList.append(list(map(int, data[i].split('|'))))
#print(ruleList)
#print()

#organize list of rules into lists of pages that must come after the entry index
rules = [[] for i in range(100)]
for i in range(len(ruleList)):
    rules[ruleList[i][0]].append(ruleList[i][1])
#print(rules)
#print()

#list of page collections to examine
pages = []
for i in range(midPoint + 1, len(data)):
    pages.append(list(map(int, data[i].split(','))))
#print(pages)
#print()

p1sum = 0
p2sum = 0

def validate(row, ruleData):
    j = len(row) - 1
    while j >= 0:
        k = j - 1
        while k >= 0:
            for x in ruleData[row[j]]:
                if row[k] == x:
                    return 0
            k = k - 1
        j = j - 1
    return row[len(row) >> 1]

def ruleSwap(row, ruleData):
    j = len(row) - 1
    while j >= 0:
        k = j - 1
        while k >= 0:
            for x in ruleData[row[j]]:
                if row[k] == x:
                    row[j], row[k] = row[k], row[j]
                    return
            k = k - 1
        j = j - 1

for i in range(len(pages)):
    targetRow = pages[i]
    found = validate(targetRow, rules)
    if (found > 0):
        p1sum = p1sum + found
        continue
    swapCount = 0
    while (found == 0):
        ruleSwap(targetRow, rules)
        swapCount = swapCount + 1
        found = validate(targetRow, rules)
    print(swapCount)
    p2sum = p2sum + found

print()

print("Problem 1")
print(p1sum)

print("Problem 2")
print(p2sum)
