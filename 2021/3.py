# AHH SO MESSY

file = open("3.input")
lines = list(map(lambda x : x.strip(), file.readlines()))
common = []

for char in lines[0]:
    common.append(0)

for line in lines:
    line = line.strip()
    for i in range(0, len(line)):
        if line[i] == "0":
            common[i] -= 1
        else:
            common[i] += 1

gamma = 0
epsilon = 0

for i in range(len(common) - 1, -1, -1):
    if common[i] > 0:
        gamma += 2 ** (len(common) - i - 1)
    else:
        epsilon += 2 ** (len(common) - i - 1)

print(gamma * epsilon)

def findCommon(l, index):
    c = 0
    for line in l:
        if line[index] == "1":
            c += 1
        else:
            c -= 1

    if c >= 0: return 1
    else: return 0

currentIndex = 0
common = list(map(lambda x : int((x / abs(x) + 1) / 2), common))

filtered = list(filter(lambda x : int(x[currentIndex]) == common[currentIndex], lines))
while len(filtered) > 1:
    currentIndex += 1
    c = findCommon(filtered, currentIndex)
    filtered = list(filter(lambda x : int(x[currentIndex]) == c, filtered))

o2 = int(filtered[0], 2)

currentIndex = 0
filtered = list(filter(lambda x : int(x[currentIndex]) != common[currentIndex], lines))
while len(filtered) > 1:
    currentIndex += 1
    c = findCommon(filtered, currentIndex)
    filtered = list(filter(lambda x : int(x[currentIndex]) != c, filtered))

co2 = int(filtered[0], 2)

print(o2 * co2)