import re

file = open("8.input")
data = [0] * 11
for line in file:
    split = line.split()
    segments = split[:10]
    output = split[11:]

    for segment in output:
        if len(segment) == 2:
            data[1] += 1
        elif len(segment) == 4:
            data[4] += 1
        elif len(segment) == 3:
            data[7] += 1
        elif len(segment) == 7:
            data[8] += 1

print(data[1] + data[4] + data[7] + data[8])
        