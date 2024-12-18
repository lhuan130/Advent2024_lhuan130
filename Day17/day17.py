#GET DATA FROM FILE
f = open("input.txt", 'r')
data = f.readlines()
f.close()
print(data)

import re

originalRegs = [51064159,0,0]
originalis = originalRegs[0]
#for i in range(3):
#  reg[i] = int(data[i].split(' ')[2])
opdata = list(map(int, re.findall('\d+', data[4])))

print(originalRegs)
print(opdata)

def comboOperand(operand, reg):
  if operand >= 0 and operand < 4:
    return operand
  elif operand == 4:
    return reg[0]
  elif operand == 5:
    return reg[1]
  elif operand == 6:
    return reg[2]
  else:
    return None

def runProgram(rA, rB, rC):
  reg = [rA, rB, rC]
  runInst = 0
  printList = []
  while runInst < len(opdata):
    notJumped = True
    opcode = opdata[runInst]
    openum = opdata[runInst + 1]
    optype = ""
    #print(runInst, opcode, openum)
    if opcode==0:
      reg[0] = int(reg[0] / (2 ** comboOperand(openum,reg)))
      optype = "A = A / 2**combop"
    elif opcode==1:
      reg[1] = reg[1] ^ openum
      optype = "B = B xor litop"
    elif opcode==2:
      reg[1] = comboOperand(openum,reg) % 8
      optype = "B = combop % 8"
    elif opcode==3 and reg[0] != 0:
      notJumped = False
      runInst = openum
      optype = "jump A==0 litop"
    elif opcode==4:
      reg[1] = reg[1] ^ reg[2]
      optype = "B=BxorC"
    elif opcode==5:
      opCalc = comboOperand(openum,reg) % 8
      printList.append(opCalc)
      optype = "print "+str(opCalc)
    elif opcode==6:
      reg[1] = int(reg[0] / (2 ** comboOperand(openum,reg)))
      optype = "B = A / 2 ** combop" 
    else:#opcode 7
      reg[2] = int(reg[0] / (2 ** comboOperand(openum,reg)))
      optype = "C = A / 2 ** combop"
    #print(reg, optype)
    if notJumped:
      runInst += 2
    #print()
  #print(",".join(list(map(str, printList))))
  return printList

print("Initial")
expected = tuple(runProgram(51064159,0,0))
print(expected)

found = False
tar = int(51064159 / 2)
while not found:
  anotherResult = tuple(runProgram(tar,0,0))
  #print(expected)
  #print(anotherResult)
  #print(tar)
  #print()
  if anotherResult == expected:
    found = True
    print("FOUND")
  tar += 1
  break
