file = open("1.input")
lines = file.readlines()

prev = int(lines[0])
counter = 0

for n in map(int, lines[1::]):
    if n > prev:
        counter += 1
    prev = n

print(counter)

counter = 0
prevsum = -1

for n in range(0, len(lines) - 2, 1):
    n1 = int(lines[n])
    n2 = int(lines[n + 1])
    n3 = int(lines[n + 2])

    sum = n1 + n2 + n3

    if prevsum > 0 and sum > prevsum:
        counter += 1
    prevsum = sum

print(counter)