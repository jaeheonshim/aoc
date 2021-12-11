file = open("9.input")
linelen = len(file.readline().strip())
file.seek(0)

heightmap = []
heightmap.append([10] * (linelen + 2))
basins = []
n = 0

for line in file:
    data = [10] + list(map(int, line.strip())) + [10]
    heightmap.append(data)


heightmap.append([10] * (linelen + 2))

sum = 0

for row in range(1, len(heightmap) - 1):
    for col in range(1, len(heightmap[row]) - 1):
        value = heightmap[row][col]
        if value < heightmap[row - 1][col] and value < heightmap[row][col - 1] and value < heightmap[row + 1][col] and value < heightmap[row][col + 1]:
            sum += value + 1
            basins.append((row, col))
            n += 1

print(sum)

traversed = set()

def parsebasin(row, col):
    sum = 1

    if row >= len(heightmap) - 1 or row < 1 or col >= len(heightmap[0]) - 1 or col < 1 or (row, col) in traversed or heightmap[row][col] == 9:
        return 0

    traversed.add((row, col))

    if heightmap[row - 1][col] - heightmap[row][col] >= 0:
        sum += parsebasin(row - 1, col)
    if heightmap[row][col - 1] - heightmap[row][col] >= 0:
        sum += parsebasin(row, col - 1)
    if heightmap[row][col + 1] - heightmap[row][col] >= 0:
        sum += parsebasin(row, col + 1)
    if heightmap[row + 1][col] - heightmap[row][col] >= 0:
        sum += parsebasin(row + 1, col)
    
    return sum
    
basin_sizes = []

for basin in basins:
    traversed.clear()
    basin_size = parsebasin(*basin)
    basin_sizes.append(basin_size)

basin_sizes.sort(reverse=True)

print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])