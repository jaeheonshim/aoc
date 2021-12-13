file = open("13.input")

points = []
folds = []

def foldy(line):
	for i in range(len(points)):
		if points[i][1] > line:
			points[i] = (points[i][0], line - (points[i][1] - line))

def foldx(line):
	for i in range(len(points)):
		if points[i][0] > line:
			points[i] = (line - (points[i][0] - line), points[i][1])

def fold(coords):
	if not coords[0]:
		foldy(coords[1])
	else:
		foldx(coords[0])

for line in file:
	if line.startswith("fold along y"):
		folds.append((0, int(line[13:])))
	elif line.startswith("fold along x"):
		folds.append((int(line[13:]), 0))
	elif line.strip():
		parts = line.split(",")
		points.append((int(parts[0].strip()), int(parts[1].strip())))	

fold(folds[0])
print(len(set(points)))

for i in range(1, len(folds)):
	fold(folds[i])

maxX = 0
maxY = 0

for point in set(points):
	maxX = max(point[0], maxX)
	maxY = max(point[1], maxY)

grid = [["." for j in range(maxX + 1)] for i in range(maxY + 1)]

for point in set(points):
	grid[point[1]][point[0]] = "#"

for line in grid:
	print("".join(line))
