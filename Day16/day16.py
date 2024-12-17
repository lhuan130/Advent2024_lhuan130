f = open("input.txt", 'r')
data = (f.read().strip()).split('\n')
f.close()
data = [list(i) for i in data]
sRow = -1
sCol = -1
for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == 'E':
      continue
    elif data[i][j] == 'S':
      sRow = i
      sCol = j
    elif data[i][j] != '#':
      data[i][j] = '.'
for line in data:
  print("".join(line))

#directions: 0N, 1E, 2S, 3W
curD = 1#E starting
offSets = {
  0:[-1,0],#N
  1:[0,1],#E
  2:[1,0],#S
  3:[0,-1],#W
}

from collections import deque
from heapq import heappush, heappop
visitQ = []#score, row, col, rowChange, colChange
visited = set()
heappush(visitQ, (0, sRow, sCol, 0, 1))
#traverse
optimum = 100000000
while visitQ:
  score, row, col, rowm, colm = heappop(visitQ)
  if data[row][col] == 'E':
    optimum = score
    print("Optimal:",optimum)
    break
  visited.add((row, col, rowm, colm))
  for nscore, nextRow, nextCol, nextRowm, nextColm in [
    (score + 1, row + rowm, col + colm, rowm, colm),
    (score + 1000, row, col, colm, -rowm),
    (score + 1000, row, col, -colm, rowm)
  ]:
    if data[nextRow][nextCol] != '#' and (nextRow, nextCol, nextRowm, nextColm) not in visited:
      heappush(visitQ, (nscore, nextRow, nextCol, nextRowm, nextColm))

#use optimum score to now traverse for "all paths"
visitQ = []
visited = dict()#now also stores optimal score to reach a path
bt = dict()#stores all ways to optimally reach a point
endStates = []
#starting point has no source path
heappush(visitQ, (0, sRow, sCol, 0, 1))
while visitQ:
  score, row, col, rowm, colm = heappop(visitQ)
  if score > visited.get((row, col, rowm, colm), optimum):#if there is a better score at reaching that path, don't bother continuing here
    continue
  else:
    visited[(row, col, rowm, colm)] = score #point at which optimal for a spot is set if not discontinued previously
  if data[row][col] == 'E':
    if score > optimum: #once you are beyond the optimum score at the end, stop
      break
    endStates.append((row, col, rowm, colm))
  for nscore, nextRow, nextCol, nextRowm, nextColm in [
    (score + 1, row + rowm, col + colm, rowm, colm),
    (score + 1000, row, col, colm, -rowm),
    (score + 1000, row, col, -colm, rowm)
  ]:
    if data[nextRow][nextCol] != '#':
      lowScore = visited.get((nextRow, nextCol, nextRowm, nextColm), optimum)
      if nscore > lowScore:
        continue
      elif nscore < lowScore:
        bt[(nextRow, nextCol, nextRowm, nextColm)] = set()
        visited[(nextRow, nextCol, nextRowm, nextColm)] = nscore
      if (nextRow, nextCol, nextRowm, nextColm) not in bt:
        bt[(nextRow, nextCol, nextRowm, nextColm)] = set()
      bt[(nextRow, nextCol, nextRowm, nextColm)].add((row, col, rowm, colm))
      heappush(visitQ, (nscore, nextRow, nextCol, nextRowm, nextColm))

checkStates = deque(endStates)
seen = set(endStates)
while checkStates:
  for last in bt.get(checkStates.popleft(), []):
    if last not in seen:
      seen.add(last)
      checkStates.append(last)

print("OPTIMAL PATH PLACES",len({(r,c)for r,c,_,_ in seen}))
