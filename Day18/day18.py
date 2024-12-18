f = open("input.txt", 'r')
data = (f.read().strip()).split('\n')
f.close()
for i in range(len(data)):
  data[i] = tuple(map(int, data[i].split(",")))
#print(data)

room = [['.' for i in range(71)] for i in range(71)]

blocked = set()

for i in range(1024):
  rowC, colC = data[i]
  blocked.add((rowC, colC))

#for row in room:
#  print("".join(row))

from heapq import heappush, heappop
def runTraverse():
  pathMem = [(0,0,0)]#score,row,col
  visited = set()
  while len(pathMem)>0:
    curScore,nr,nc = heappop(pathMem)
    if (nr,nc) in visited: continue
    visited.add((nr,nc))
    if nr==nc and nc==70:
      return curScore
    if (nr>0) and (nr-1,nc) not in blocked:#up
      heappush(pathMem, (curScore+1,nr-1,nc))
    if (nr<len(room)-1) and (nr+1,nc) not in blocked:#down
      heappush(pathMem, (curScore+1,nr+1,nc))
    if (nc>0)  and (nr,nc-1) not in blocked:#left
      heappush(pathMem, (curScore+1,nr,nc-1))
    if (nc<len(room[nr])-1) and (nr,nc+1) not in blocked:#right
      heappush(pathMem, (curScore+1,nr,nc+1))
  return -1

print("Problem 1",runTraverse())

first,last = 0,len(data)
x = int(len(data) / 2)
while first!=last:
  #print(x)
  blocked = {z for z in data[:x]}
  result = runTraverse()
  print(first,x,last,result)
  print(data[x-1])
  if (result < 0):#blocked
    last = x
  else:
    first = x
  x = int((first + last) / 2)
  a=input("Try")
#NOTE: manual handling needed at end to check first blocking coord
