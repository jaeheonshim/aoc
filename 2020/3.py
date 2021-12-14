file = open("3.input")
trees = []
for line in file:
	trees.append(list(line.strip()))

x = 3
count = 0
for i in range(1, len(trees)):
	if(trees[i][x] == "#"): count += 1
	x += 3
	x %= len(trees[0])	

print(count)

def checkSlope(right, down):
	x = right
	count = 0
	for i in range(down, len(trees), down):
		if(trees[i][x] == "#"): count += 1
		x += right
		x %= len(trees[0])
	return count

product = checkSlope(1, 1) * checkSlope(3, 1) * checkSlope(5, 1) * checkSlope(7, 1) * checkSlope(1, 2)
print(product)
