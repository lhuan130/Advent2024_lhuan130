f = open("input.txt", 'r')
data = f.readlines()
f.close()

towels = (data[0].strip()).split(", ")
designs = []
for i in range(2, len(data)):
  designs.append(data[i].strip())
towels = sorted(towels, key=len)
towels.reverse()
#print(towels)

from functools import cache
@cache
def tryPat(longPat, start):
  if start==len(longPat):
    return 1
  valid = 0
  for towel in towels:
    if longPat[start:].startswith(towel):
      #print(towel)
      valid += tryPat(longPat, start+len(towel))
  return valid

possible = 0
totalways = 0
for design in designs:
  ways = tryPat(design, 0)
  if ways>0:
    print("Possible:",design)
    possible += 1
  totalways += ways
print("Possible:",possible)
print("Ways: ",totalways)
