def puzzleOne():
  file = open("input.txt")
  lines = file.readlines();

  bits = []
  gammaBinaryStr = ''
  epsilonBinaryStr = ''
  numberOfLines = len(lines)
  numberOfBits = len(lines[0].strip())

  print(numberOfBits)
  for i in range(0, numberOfBits):
    bits.append(0)

  for line in lines:
    for i in range(0, numberOfBits-1):
      bits[i] += int(line[i]) 

  for bit in bits:
    if bit > numberOfLines/2:
      gammaBinaryStr += "1"
      epsilonBinaryStr += "0"
    else:
      gammaBinaryStr += "0"
      epsilonBinaryStr += "1"
  
  print(len(line[0]))
  print(gammaBinaryStr)
  gamma = int(gammaBinaryStr, 2)
  epsilon = int(epsilonBinaryStr, 2)
  print("Power consumption: " + str(gamma*epsilon))

def puzzleTwo():
  file = open("input.txt")  
  lines = file.readlines()

  oxygenRating = getRating(list(lines), "oxygen")
  co2Rating = getRating(list(lines), "co2")

  print("Life support rating - " + str(oxygenRating * co2Rating))


def getRating(lines, type):
  print("Number of lines - " + str(len(lines))) 
  bitIndex = 0

  while len(lines) > 1:
    numberOfLinesRemaining = len(lines)
    print(numberOfLinesRemaining)
    setBitCounter = 0
    bitSet = 0
    for line in lines: 
       setBitCounter += int(line[bitIndex]) 
    if type == "oxygen":
      if numberOfLinesRemaining - setBitCounter <= setBitCounter:
          bitSet = 1
    if type == "co2":
      if setBitCounter < numberOfLinesRemaining-setBitCounter:
        bitSet = 1 
    lines = [x for x in lines if int(x[bitIndex]) == bitSet]

    bitIndex += 1
    if bitIndex == 12:
      bitIndex = 0
    
  return int(lines[0],2)


puzzleTwo()