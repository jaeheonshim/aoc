file = open("6.input")
lines = file.readlines()
input = list(map(int, lines[0].split(",")))

def tickDay():
    global input
    newfish = []
    for i in range(len(input)):
        input[i] -= 1
        if(input[i] < 0):
            newfish.append(8)
            input[i] = 6

    input += newfish
    
for i in range(80):
    tickDay()

print(len(input))