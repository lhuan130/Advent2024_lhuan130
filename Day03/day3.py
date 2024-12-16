f = open("input.txt")
lines = f.readlines()
f.close()

import re

uncsum = 0
enabled = True
for line in lines:
    mList = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
    for instr in mList:
        if instr[0] == 'd':
            if instr[2] == '(':
                enabled = True
            else:
                enabled = False
                #enabled = True
        elif enabled:
            nums = re.findall("[0-9]{1,3}", instr)
            uncsum += (int(nums[0]) * int(nums[1]))

print(uncsum)

#Problem 1 did not check for do/don't enable/disable; that is the only diff
