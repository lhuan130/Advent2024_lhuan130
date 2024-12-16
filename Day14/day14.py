f = open("input.txt", 'r')
data = f.readlines()
f.close()

import re
rowLen = 101
colLen = 103
#input processing
px = []
py = []
vx = []
vy = []
for line in data:
  nums = re.findall('-*\d+', line)
  px.append(int(nums[0]))
  py.append(int(nums[1]))
  vx.append(int(nums[2]))
  vy.append(int(nums[3]))

#print(len(px))

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for i in range(len(px)):
  for j in range(100):
    px[i] = (px[i] + vx[i] + rowLen) % rowLen
    py[i] = (py[i] + vy[i] + colLen) % colLen
  #px[i] = (((px[i] + (100 * (vx[i]))) % rowLen) + rowLen) % rowLen
  #py[i] = (((py[i] + (100 * (vy[i]))) % colLen) + colLen) % colLen
  if px[i] > (int(rowLen / 2)):
    if py[i] > (int(colLen / 2)):
      q1 += 1
    elif py[i] < (int(colLen / 2)):
      q2 += 1
  elif px[i] < (int(rowLen / 2)):
    if py[i] > (int(colLen / 2)):
      q3 += 1
    elif py[i] < (int(colLen / 2)):
      q4 += 1
print(q1*q2*q3*q4)

print("P2")
cycles = 0
f = open("input.txt", 'r')
data = f.readlines()
f.close()
px = []
py = []
vx = []
vy = []
for line in data:
  nums = re.findall('-*\d+', line)
  px.append(int(nums[0]))
  py.append(int(nums[1]))
  vx.append(int(nums[2]))
  vy.append(int(nums[3]))

#import numpy as np
#px = np.array(px)
#py = np.array(py)

round = 0
scoreMin = 125**4
minRound = 0
for k in range(10000):
  round += 1
  for i in range(len(px)):
    px[i] = (px[i] + vx[i] + rowLen) % rowLen
    py[i] = (py[i] + vy[i] + colLen) % colLen
  q1 = 0
  q2 = 0
  q3 = 0
  q4 = 0
  for i in range(len(px)):
    if px[i] > (int(rowLen / 2)):
      if py[i] > (int(colLen / 2)):
        q1 += 1
      elif py[i] < (int(colLen / 2)):
        q2 += 1
    elif px[i] < (int(rowLen / 2)):
      if py[i] > (int(colLen / 2)):
        q3 += 1
      elif py[i] < (int(colLen / 2)):
        q4 += 1
  curScore = q1*q2*q3*q4
  if curScore < scoreMin:
    scoreMin = curScore
    minRound = round
print(minRound)
