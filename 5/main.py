def puzzleOne():
  file = open("input.txt")
  lines = file.readlines()
  coordArray = cleanInputLines(lines)
  
  dangerArray = initialiseDangerArray(coordArray) 

  for coord in coordArray:
    markDangerArray(coord,dangerArray)

  danger = countDangerCells(dangerArray)
  print(danger)
  
def outputDangerArray(dangerArray):
  outputFile = open("output.txt", "w")
  for row in dangerArray:
    outputFile.write(str(row)+"\n")
  
  outputFile.close()
    
def countDangerCells(dangerArray):
  counter = 0
  for dangerCol in dangerArray:
    for dangerCell in dangerCol: 
      if dangerCell > 1:
        counter+=1
  return counter

def markDangerArray(coord, dangerArray):
  lowY = min(coord[1], coord[3])
  highY = max(coord[1],coord[3])
  lowX = min(coord[0], coord[2])
  highX = max(coord[0],coord[2])

  if not isDiagonal(coord):
    for x in range(lowX, highX+1):
      for y in range(lowY, highY+1):
        dangerArray[x][y] += 1
  else:
     xInc = 1
     if coord[0] > coord[2]:
       xInc = -1
     yInc = 1
     if coord[1] > coord[3]:
       yInc = -1
     y = coord[1]
     for x in range(coord[0], coord[2]+xInc, xInc):
       dangerArray[x][y] += 1
       y += yInc

def initialiseDangerArray(coordArray):
  maxX = 0
  maxY = 0
  for coord in coordArray:
    maxX = max(maxX, coord[0], coord[2])
    maxY = max(maxY, coord[1],coord[3])

  maxX +=1
  maxY +=1
  dangerArray = []
  for x in range(0, maxX):
    row = []
    for y in range(0, maxY):
      row.append(0) 
    dangerArray.append(row)

  return dangerArray

def cleanInputLines(lines):
  coordinateArray = []
  for line in lines:
    line = line.strip()
    line = line.replace(" -> ", ",")
    numbers = line.split(",")
    map_object = map(int, numbers)
    coordinateArray.append(list(map_object))

  resultCoordArray = []
  for i in range(0, len(coordinateArray)):
    if coordinateArray[i][0] == coordinateArray[i][2] or coordinateArray[i][1] == coordinateArray[i][3] or isDiagonal(coordinateArray[i]):
      resultCoordArray.append(coordinateArray[i])

  return resultCoordArray

def isDiagonal(coord):
  lowY = min(coord[1], coord[3])
  highY = max(coord[1],coord[3])
  lowX = min(coord[0], coord[2])
  highX = max(coord[0],coord[2])
  if highX - lowX == highY - lowY:
    return True
  return False

puzzleOne()