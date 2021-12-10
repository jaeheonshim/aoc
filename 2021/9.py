file = open("9.input")
sum = 0
linelen = len(file.readline())
file.seek(0)

heightmap = []
heightmap.append([10] * linelen)

for line in file:
    data = [10] + list(map(int, line.strip())) + [10]
    heightmap.append(data)

heightmap.append([10] * linelen)

sum = 0

for row in range(1, len(heightmap) - 1):
    for col in range(1, len(heightmap[row]) - 1):
        value = heightmap[row][col]
        if value < heightmap[row - 1][col] and value < heightmap[row][col - 1] and value < heightmap[row + 1][col] and value < heightmap[row][col + 1]:
            sum += value + 1

print(sum)