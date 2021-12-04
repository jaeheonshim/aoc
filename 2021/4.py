file = open("4.input")
lines = file.readlines()

randInput = list(map(int, map(lambda x : x.strip(), lines[0].split(","))))

boardList = []

for i in range(2, len(lines), 6):
    board = []
    for j in range(0, 5):
        row = []
        for num in lines[i + j].split(" "):
            if num:
                row.append(int(num.strip()))
        board.append(row)
    boardList.append(board)

def submitInt(num):
    global boardList
    for boardIndex in range(0, len(boardList)):
        for i in range(0, 5):
            for j in range(0, 5):
                if boardList[boardIndex][i][j] == num:
                    boardList[boardIndex][i][j] = -1

def findWinners():
    winners = []
    for boardIndex in range(0, len(boardList)):
        for i in range(0, 5):
            if boardList[boardIndex][i][0] == boardList[boardIndex][i][1] == boardList[boardIndex][i][2] == boardList[boardIndex][i][3] == boardList[boardIndex][i][4] == -1:
                winners.append(boardIndex)
                break
            if boardList[boardIndex][0][i] == boardList[boardIndex][1][i] == boardList[boardIndex][2][i] == boardList[boardIndex][3][i] == boardList[boardIndex][4][i] == -1:
                winners.append(boardIndex)
                break

    return winners

for num in randInput:
    lastNum = num
    submitInt(num)
    winners = findWinners()
    if(len(winners) > 0):
        winner = winners[0]
        break

sum = 0
winner = boardList[winner]
for row in winner:
    for col in row:
        if col > 0:
            sum += col

print(sum * lastNum)