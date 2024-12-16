f = open('input.txt')
lines = f.readlines()
f.close()

l1 = []
l2 = []
countMap = dict()

for line in lines:
    txt = (line.strip()).split('   ')
    l1.append(int(txt[0]))
    b = int(txt[1])
    l2.append(b)
    newCt = 1 + countMap.get(b, 0)
    countMap.update({b: newCt})
l1.sort()
l2.sort()

i = 0
diff = 0
sim = 0
while i < len(l1):
    diff += abs(l1[i]-l2[i])
    sim += l1[i] * countMap.get(l1[i], 0)
    i += 1
print("Problem 1")
print(diff)
print("Problem 2")
print(sim)

