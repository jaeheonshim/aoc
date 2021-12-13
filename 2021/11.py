file = open("11.input")
grid = []
for line in file:
    grid.append([int(c) for c in line if c.isnumeric()])

def step():
    flash_sum = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            grid[i][j] += 1

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] > 9: flash_sum += flash(i, j)

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == -1: grid[i][j] = 0

    return flash_sum

def flash(r, c):
    flash_count = 1
    grid[r][c] = -1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (r + i) >= len(grid) or (r + i) < 0 or (c + j) >= len(grid[r]) or (c + j) < 0: continue
            if grid[r + i][j + c] == -1: continue
            grid[r + i][j + c] += 1
            if grid[r + i][j + c] > 9: flash_count += flash(r + i, j + c)

    return flash_count

total_flashes = 0
for i in range(0, 100):
    total_flashes += step()

print(total_flashes)

def sum2d(arr2d):
    total = 0
    for arr in arr2d:
        total += sum(arr)

    return total

steps = 100
while sum2d(grid) != 0:
    step()
    steps += 1

print(steps)
