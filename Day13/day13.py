f = open("input.txt", 'r')
data = f.readlines()
f.close()

#input processing
import re
ax = []
ay = []
bx = []
by = []
px = []
py = []
#atimes = []
#btimes = []
for i in range(0, len(data), 4):
    nums = re.findall('\d+', data[i])
    ax.append(int(nums[0]))
    ay.append(int(nums[1]))
    nums = re.findall('\d+', data[i+1])
    bx.append(int(nums[0]))
    by.append(int(nums[1]))
    nums = re.findall('\d+', data[i+2])
    px.append(int(nums[0]))
    py.append(int(nums[1]))

print(ax[0], ay[0])
print(bx[0], by[0])
print(px[0], py[0])

#problem 1
import math
ans = 0
for i in range(len(ax)):
    bTime = max(math.ceil(px[i] / bx[i]), math.ceil(py[i] / by[i]))
    while bTime >= 0:
        if (px[i] - bTime*bx[i]) % ax[i] == 0 and (py[i] - bTime*by[i]) % ay[i] == 0:
            aTimeX = int((px[i] - bTime*bx[i]) / ax[i])
            aTimeY = int((py[i] - bTime*by[i]) / ay[i])
            if aTimeX == aTimeY:
                ans += 3*aTimeX;
                ans += bTime;
                break
        bTime -= 1

print("PROBLEM 1:",ans)
ans = 0
for i in range(len(px)):
    px[i] += 10000000000000
    py[i] += 10000000000000

#from functools import reduce
#def factors(n):
#    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#pyf = [list(factors(x)) for x in py]
#for i in range(pyf):
#    pyf[i].sort()
#    break
#print(pyf[0])

import numpy as np
for i in range(len(px)):
    eqs = np.array([[ax[i], bx[i]],[ay[i],by[i]]])
    tot = np.array([px[i], py[i]])
    sol = np.linalg.solve(eqs, tot)
    if round(sol[0])*ax[i] + round(sol[1])*bx[i] != px[i] or round(sol[0])*ay[i] + round(sol[1])*by[i] != py[i]:
        continue
    ans += 3 * sol[0] + sol[1]
    

print("PROBLEM 2:",ans)
