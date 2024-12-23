f = open("input.txt", 'r')
data = (f.read().strip()).split('\n')
f.close()
data = list(map(list, data))

rbounds = len(data)
cbounds = len(data[0])
sr,sc = 0,0
er,ec = 0,0
sfound, efound = False,False
for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == 'S':
      sr,sc = i,j
      sfound = True
    elif data[i][j] == 'E':
      er,ec = i,j
      efound = True
    if sfound and efound:
      break
  if sfound and efound:
    break

#Default traversal search is easier given single path provided 
reachDist = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
reachDist[sr][sc] = 0
row,col = sr,sc
while (row,col) != (er,ec):
  for nrow, ncol in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
    if (nrow < 0 or nrow == rbounds or ncol < 0 or ncol == cbounds) or reachDist[nrow][ncol] != -1 or data[nrow][ncol] == '#':
      continue
    reachDist[nrow][ncol] = 1 + reachDist[row][col]
    row = nrow
    col = ncol

#CODE TO GENERATE LIST OF USEFUL MOVES
def possible_moves(jumpSize, rowStart, colStart):
  moveList = []
  jumpLim = jumpSize+1
  for drow in range(jumpSize+1):
    dcol = jumpSize - drow
    for nr,nc in {(rowStart+drow,colStart+dcol),(rowStart+drow,colStart-dcol),(rowStart-drow,colStart+dcol),(rowStart-drow,colStart-dcol)}:
      moveList.append((nr,nc))
  return moveList

#PROBLEM 1
jumpset = set() #row,col,nrow,ncol; the order doesn't matter if the checks only happen in a specific direction
for row in range(len(data)):
  for col in range(len(data[row])):
    if reachDist[row][col] < 0: continue
#    if data[row][col] == '#': continue
    for nrow,ncol in possible_moves(2, row, col):
      if (nrow < 0 or nrow >= rbounds or ncol < 0 or ncol >= cbounds) or data[nrow][ncol] == '#': continue
      if reachDist[nrow][ncol] - reachDist[row][col] >= 102:
        jumpset.add((row,col,nrow,ncol))
      elif reachDist[row][col] - reachDist[nrow][ncol] >= 102:
        jumpset.add((nrow,ncol,row,col))
print("PROBLEM 1: >100 time saved w/ 2 skips - ",len(jumpset))

#PROBLEM 2
jumpset = set()
for row in range(len(data)):
  for col in range(len(data[row])):
    if reachDist[row][col] < 0: continue
    for jumpLen in range(2,21):
      safeLen = 99 + jumpLen
      possible_now = possible_moves(jumpLen,row,col)
      for nrow,ncol in possible_now:
        if nrow < 0 or nrow >= rbounds or ncol < 0 or ncol >= cbounds or reachDist[nrow][ncol] < 0: continue
        if reachDist[nrow][ncol] - reachDist[row][col] >= safeLen:
          jumpset.add((row,col,nrow,ncol))
        elif reachDist[row][col] - reachDist[nrow][ncol] >= safeLen:
          jumpset.add((nrow,ncol,row,col))
print("PROBLEM 2: >100 time saved w/ up to 20 skips - ",len(jumpset))








