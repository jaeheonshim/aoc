file = open("6.input")
lines = file.readlines()
input = list(map(int, lines[0].split(",")))
fishDict = {}
fishes = []

for fish in input:
    if fish not in fishDict:
        fishDict[fish] = 1
    else:
        fishDict[fish] = fishDict[fish] + 1

for timer in fishDict:
    fishes.append([timer, fishDict[timer]])

def tickDay():
    global fishes

    newfish = 0

    for fish in fishes:
        fish[0] -= 1
        if fish[0] < 0:
            newfish += fish[1]
            fish[0] = 6
    
    fishes.append([8, newfish])

# don't bother reduce lol

for i in range(256):
    tickDay()

sum = 0
for fish in fishes:
    sum += fish[1]

print(sum)