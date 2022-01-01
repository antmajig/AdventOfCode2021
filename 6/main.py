def puzzleOne():
  file = open("input.txt")
  input = file.readline()
  input = input.split(",")
  fish = list(map(int, input))

  for day in range(0,256):
    spawn = 0
    for f in range(0, len(fish)):
      fish[f] -= 1
      if fish[f] == -1:
        fish[f] = 6 
        spawn += 1
    for i in range(0,spawn):
      fish.append(8)
    print(day)

  print(len(fish)) 


def puzzleTwo():
  file = open("input.txt")
  input = file.readline()
  input = input.split(",")
  input = list(map(int, input))
  fish = []
  for i in range(0,9):
    fish.append(input.count(i))
  
  print(len(fish))
  print(fish)
  for day in range(0,256):
    spawn = fish[0]
    fish[7] += spawn 
    fish[0] = 0
    fish = rotate(fish, -1)
    fish[8] = spawn
    print(fish)

  fishCount = 0
  for f in fish:
    fishCount += f
  print(fishCount)

def rotate(l, x):
  return l[-x:] + l[:-x]
puzzleTwo()