file = open("2.input")
lines = file.readlines()

x = 0
y = 0

for line in lines:
    split = line.split()
    direction = split[0]
    value = int(split[1])

    if direction == "forward":
        x += value
    elif direction == "up":
        y -= value
    else:
        y += value

print(x * y)

aim = 0
x = 0
y = 0
for line in lines:
    split = line.split()
    direction = split[0]
    value = int(split[1])

    if direction == "forward":
        x += value
        y += value * aim
    elif direction == "up":
        aim -= value
    else:
        aim += value

print(x * y)