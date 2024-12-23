f = open("input.txt", 'r')
data = list(map(int, (f.readlines()[0]).split(" ")))
f.close()
print(data)

test = [0]
print()

from functools import cache
@cache
def blinkStones(stone, iterV):
    if iterV == 0:
        return 1
    counter = 0
    if stone == 0:
        return blinkStones(1, iterV-1)
    elif len(str(stone)) % 2 == 0:
        val = str(stone)
        l = int(val[:len(val)>>1])
        r = int(val[len(val)>>1:])
        return blinkStones(l, iterV-1) + blinkStones(r, iterV-1)
    else:
        return blinkStones(stone*2024, iterV-1)

counter = 0
count = 75
for x in data:
    counter += blinkStones(x, count)

print("Iterations: ", count)
print(counter)
print()
