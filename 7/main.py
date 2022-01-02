def puzzleOne():
  file = open("input.txt")
  input = file.readline()
  input = input.split(",")
  crabs = map(int, input)

  minCrab = min(crabs)
  maxCrab = max(crabs)
  indexPairList = []
  for i in range(minCrab, maxCrab+1):
    i_sum = 0
    for crab in crabs:
      i_sum += abs(i - crab)
    pair = (i,i_sum)
    indexPairList.append((i,i_sum))  

  print(min(indexPairList, key = lambda t: t[1])) 


def puzzleTwo():
  file = open("input.txt")
  input = file.readline()
  input = input.split(",")
  crabs = map(int, input)

  minCrab = min(crabs)
  maxCrab = max(crabs)
  indexPairList = []
  for i in range(minCrab, maxCrab+1):
    i_sum = 0
    for crab in crabs:
      steps = abs(i-crab)
      i_sum += (pow(steps,2) + steps) / 2
    pair = (i,i_sum)
    indexPairList.append((i,i_sum))  

  print(min(indexPairList, key = lambda t: t[1])) 
puzzleTwo()