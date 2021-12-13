import re

file = open("5.input")
lines = file.readlines()

def parseLine(line):
    match = re.findall("(\d*),(\d*)\s->\s(\d*),(\d*)", line)[0]
    return ((int(match[0]), int(match[1])), (int(match[2]), int(match[3])))

hDict = {}
vDict = {}
vert = []

for line in lines:
    points = parseLine(line)
    if points[0][0] == points[1][0]: # Vertical line
        vDict.setdefault(points[0][0], []).append(points)
    elif points[0][1] == points[1][1]: # Horizontal line
        hDict.setdefault(points[0][1], []).append(points)
    else:
        vert.append(points)

overlap_sum = 0

for y in range(0, 1000):
    overlap = [0] * 999
    if y in hDict:
        for line in hDict[y]:
            x1o = min(line[0][0], line[1][0])
            x1f = max(line[0][0], line[1][0])
            for j in range(x1o, x1f + 1):
                overlap[j] += 1
    for lines in vDict.values():
        for line in lines:
            y1o = min(line[0][1], line[1][1])
            y1f = max(line[0][1], line[1][1])
            if y1o <= y <= y1f:
                overlap[line[0][0]] += 1

    for line in vert:
        x1o = line[0][0]
        x1f = line[1][0]
        y1o = line[0][1]
        y1f = line[1][1]

        m = (y1f - y1o) // (x1f - x1o)
        dY = y - y1o
        newX = x1o + dY // m
        if min(x1o, x1f) <= newX <= max(x1f, x1o):
            overlap[x1o + dY // m] += 1

    overlap_count = 0
    for i in overlap:
        if i > 1:
            overlap_count += 1
    overlap_sum += overlap_count

print(overlap_sum)