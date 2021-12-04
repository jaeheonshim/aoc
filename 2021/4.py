file = open("4.input")
lines = file.readlines()

drawn_numbers = list(map(int, lines[0].split(",")))
boards = []

for i in range(2, len(lines), 6):
    boardRows = []
    for j in range(0, 5):
        row = []
        for str in lines[i + j].split(" "):
            if str.strip():
                row.append(int(str.strip()))
        boardRows.append(row)

    boards.append(boardRows)

def submitInt(num):
    for board in boards:
        for row in range(0, 5):
            for col in range(0, 5):
                if(board[row][col] == num): 
                    board[row][col] = -1

def returnWinners():
    winners = []
    for n, board in enumerate(boards):
        for i in range(0, 5):
            if (board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1) or (board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1):
                winners.append((n, board))

    return winners

def sumboard(board):
    sum = 0
    for row in board:
        for col in row:
            if col >= 0:
                sum += col
    return sum

currentI = 0
while (len(returnWinners()) == 0):
    submitInt(drawn_numbers[currentI])
    currentI += 1

winners = returnWinners()
print(sumboard(winners[0][1]) * drawn_numbers[currentI - 1])
boards.pop(winners[0][0])

while currentI < len(drawn_numbers):
    submitInt(drawn_numbers[currentI])
    currentI += 1

    winners = returnWinners()
    breakFlag = False
    popList = []
    for winner in winners:
        if len(boards) > 1:
            boards[winner[0]] = None
        else:
            breakFlag = True
            break

    boards = list(filter(lambda x: x != None, boards))

    if breakFlag: break

print(sumboard(returnWinners()[0][1]) * drawn_numbers[currentI - 1])