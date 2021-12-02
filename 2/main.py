def puzzleOne():
  file = open("./input.txt")
  lines = file.readlines()

  depth = 0
  horizontal = 0

  for line in lines:
    originalLine = line
    stringChange = False

    line = line.replace("forward ", "")
    if line != originalLine:
      horizontal += int(line)
      stringChange = True    

    line = line.replace("down ", "")
    if line != originalLine and not stringChange:
      depth += int(line)
      stringChange = True

    line = line.replace("up ", "")
    if line != originalLine and not stringChange:
      depth -= int(line)
      stringChange = True

  print(horizontal*depth)

def puzzleTwo():
  file = open("./input.txt")
  lines = file.readlines()

  depth = 0
  horizontal = 0
  aim = 0

  for line in lines:
    originalLine = line
    stringChange = False

    line = line.replace("forward ", "")
    if line != originalLine:
      horizontal += int(line)
      depth += aim * int(line)
      stringChange = True    

    line = line.replace("down ", "")
    if line != originalLine and not stringChange:
      aim += int(line)
      stringChange = True

    line = line.replace("up ", "")
    if line != originalLine and not stringChange:
      aim -= int(line)
      stringChange = True

  print(horizontal*depth)

puzzleTwo()