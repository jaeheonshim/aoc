import re

file = open("8.input")
data = [0] * 10
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

file.seek(0)

total = 0
for line in file:
    split = line.split()
    segments = split[:10]
    output = split[11:]
    numbers = [None] * 10
    sum = 0

    for segment in segments:
        if len(segment) == 2:
            numbers[1] = set(segment)
        elif len(segment) == 4:
            numbers[4] = set(segment)
        elif len(segment) == 3:
            numbers[7] = set(segment)
        elif len(segment) == 7:
            numbers[8] = set(segment)

    for segment in segments:
        if len(segment) == 5:
            if numbers[1].issubset(segment):
                numbers[3] = set(segment)
            elif (numbers[4] - numbers[7]).issubset(segment):
                numbers[5] = set(segment)
            else:
                numbers[2] = set(segment)
        elif len(segment) == 6:
            if set(numbers[4] | numbers[7]).issubset(segment):
                numbers[9] = set(segment)
            elif numbers[1].issubset(segment):
                numbers[0] = set(segment)
            else:
                numbers[6] = set(segment)

    for s in output:
        sum *= 10
        sum += numbers.index(set(s))

    total += sum

print(total)