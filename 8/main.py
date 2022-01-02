def puzzleOne():
  file = open("input.txt")
  input = file.readlines()
  lines = []
  for line in input:
    line = line.split("|")
    lines.append(line[1].split())
  
  uniqueCount = 0
  for line in lines:
    for seq in line:
      if isUnique(seq):
        uniqueCount+=1
  
  print(uniqueCount)

def puzzleTwo():
  file = open("input.txt")
  input = file.readlines()
  lines = []
  totalSum = 0
  for line in input:
    line = line.split("|")
    lineSeq = line[0].split()
    outputSeq = line[1].split()
    lineSeq = sortCharacterArray(lineSeq)
    outputSeq = sortCharacterArray(outputSeq)
    numbers = findNumbers(lineSeq)

    numberConvert = str(numbers.index(outputSeq[0]))
    numberConvert += str(numbers.index(outputSeq[1]))
    numberConvert += str(numbers.index(outputSeq[2]))
    numberConvert += str(numbers.index(outputSeq[3]))
    totalSum += int(numberConvert)
  
  print(totalSum)


  
def findNumbers(line):
  numbers = [""]*10 
  for seq in line:
    if len(seq) == 2:
      numbers[1] = seq
    if len(seq) == 3:
      numbers[7] = seq
    if len(seq) == 7:
      numbers[8] = seq
    if len(seq) == 4:
      numbers[4] = seq
      
  #find 6
  for seq in line:
    if len(seq) == 6:
      hasBoth = True
      for char in list(numbers[1]):
        if char not in seq:
          hasBoth = False

      if not hasBoth:
        numbers[6] = seq    

  #find 9
  for seq in line:
    if len(seq) == 6:
      hasBoth = True
      for char in list(numbers[4]):
        if char not in seq:
          hasBoth = False

      if hasBoth:
        numbers[9] = seq    

  #find 0
  for seq in line:
    if len(seq) == 6:
      if seq != numbers[9] and seq != numbers[6]:
        numbers[0] = seq

  
  copyNumber8 = list(numbers[8])
  for char in list(numbers[9]):
   copyNumber8.remove(char) 


  #find 2
  for seq in line:
    if len(seq) == 5:
      if copyNumber8[0] in list(seq):
        numbers[2] = seq
        
  #find 3
  for seq in line:
    if len(seq) == 5:
      hasBoth = True
      for char in list(numbers[1]):
        if char not in seq:
          hasBoth = False

      if hasBoth:
        numbers[3] = seq    
  #find 5
  for seq in line:
    if len(seq) == 5:
      if seq != numbers[2] and seq != numbers[3]:
        numbers[5] = seq

  numbers = sortCharacterArray(numbers)
  return numbers

def sortCharacterArray(numbers):
  for i in range(0, len(numbers)): 
    numbers[i] = list(numbers[i])
  
  for i in range(0, len(numbers)):
    numbers[i].sort()

  for i in range(0, len(numbers)):
    numbers[i] = "".join(numbers[i])
  
  return numbers

def isUnique(wireSeq):
  numberOfActiveSeg = len(wireSeq) 
  if numberOfActiveSeg == 2 or numberOfActiveSeg == 4 or numberOfActiveSeg == 3 or numberOfActiveSeg == 7:
    return True
  return False 

puzzleTwo()