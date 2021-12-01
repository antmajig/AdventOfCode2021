def increaseListCounter(list):
  increaseCount = 0
  input = 0

  input = int(list[0])
  for line in list:
    if int(line) > input:
      increaseCount+=1
    input = int(line)

  print("increase " + str(increaseCount))

def puzzleOne():
  print("hello")
  f = open("./input.txt", "r")
  lines = f.readlines()
  increaseListCounter(lines)

def puzzleTwo():
  f = open("./input.txt", "r")
  lines = f.readlines()
  sumSequence = []
  lineCount = len(lines)
  for i in range(0, lineCount - 2):
    sumSequence.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))

  increaseListCounter(sumSequence)
    
puzzleTwo()