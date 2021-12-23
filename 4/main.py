def puzzleOne():
  file = open("input.txt")
  lines = file.readlines()
  inputNum = lines[0]
  inputNum = inputNum.strip()
  inputNum = inputNum.split(",")
  map_object = map(int, inputNum)
  inputNum = list(map_object)

  cards = readCards(lines)

  winningCard = 0
  lastCalledNumber = 0
  for number in inputNum:
    bingo = False
    for i in range(0, len(cards)):
      markCard(cards[i],number)
      bingo = hasBingo(cards[i])
      if bingo:
        winningCard = i
        lastCalledNumber = number
        print("bingo!")
        print(winningCard)
        print(lastCalledNumber)
        break
    if bingo:
      break
  
  sum = sumOfBingoCard(cards[winningCard])
  print(sum)
  print(sum * lastCalledNumber)

def puzzleTwo():
  file = open("input.txt")
  lines = file.readlines()
  inputNum = lines[0]
  inputNum = inputNum.strip()
  inputNum = inputNum.split(",")
  map_object = map(int, inputNum)
  inputNum = list(map_object)

  cards = readCards(lines)

  lastCalledNumber = 0
  lastCard = []
  numberIndex = 0
  while len(cards) > 0:
    popThese = []
    for i in range(0,len(cards)):
      markCard(cards[i], inputNum[numberIndex])
      bingo = hasBingo(cards[i])
      if bingo:
        popThese.append(i)

    if len(cards) == 1:
     lastCard = cards[0]

    for i in range(len(popThese)-1, -1, -1):
      cards.pop(popThese[i])

    lastCalledNumber = inputNum[numberIndex]
    print(lastCalledNumber)
    print("len" + str(len(cards)))
    numberIndex += 1

  
  sum = sumOfBingoCard(lastCard)
  print(sum)
  print(sum * lastCalledNumber)

def readCards(lines):
  cards = []
  cardIndex = 0
  cards.insert(cardIndex, list())
  for i in range(2, len(lines)):
    numberStr = lines[i]
    if(len(numberStr) > 1):
      numList = numberStr.split()
      map_object = map(int, numList)
      row = list(map_object)
      cards[cardIndex].append(row)
    else:
      i += 1
      cardIndex += 1
      cards.insert(cardIndex, list())
  return cards    

def sumOfBingoCard(card):
  print(card)
  sum = 0
  for row in card:
    for value in row:
     if value != -1:
       sum += value 
  return sum

def markCard(card, number):
  for row in card:
    for i in range(0, len(row)): 
      if row[i] == number:
       row[i] = -1   

def hasBingo(card):
  #check vertical
  #transpose 2d list
  
  transposedCard = list(map(list, zip(*card)))   
  for col in transposedCard:
    colBingo = True
    for value in col:
      if value != -1:
        colBingo = False
    if colBingo:
      return True    


  #check horizonal
  for row in card:
    rowBingo = True
    for value in row:
      if value != -1:
        rowBingo = False
    if rowBingo:
      return True
  
  return False
puzzleTwo()
