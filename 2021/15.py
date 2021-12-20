class Node:
    def __init__(self, cost):
        self.cost = cost
        self.neighbors = {}
        self.distance = -1

    def addneighbor(self, neighbor):
        self.neighbors[neighbor] = neighbor.cost

def mindist(a, b):
    if a == -1: return b
    if b == -1: return a

    return min(a, b)

def dijkstra(start):
    start.distance = 0
    unvisited = {start: start.distance}
    visited = set()

    while unvisited:
        node = min(unvisited, key=unvisited.get)

        for neighbor in node.neighbors:
            if neighbor not in visited:
                neighbor.distance = mindist(neighbor.distance, node.distance + node.neighbors[neighbor])
                unvisited[neighbor] = neighbor.distance
        
        visited.add(node)
        unvisited.pop(node)


data = open("15.input")
nodes = []

for line in data:
    row = []
    for char in line.strip():
        row.append(Node(int(char)))
    nodes.append(row)

for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        if (i - 1) >= 0:
            nodes[i][j].addneighbor(nodes[i - 1][j])
        if (j - 1) >= 0:
            nodes[i][j].addneighbor(nodes[i][j - 1])
        if (i + 1) < len(nodes):
            nodes[i][j].addneighbor(nodes[i + 1][j])
        if (j + 1) < len(nodes[0]):
            nodes[i][j].addneighbor(nodes[i][j + 1])

start_node = nodes[0][0]
end_node = nodes[-1][-1]
dijkstra(start_node)
print(end_node.distance)

# PART 2 (unoptimized, takes a bit of time)

def inc(val, n):
    val += n
    while val > 9:
        val = val - 9
    return val

data.seek(0)
costs = []
for line in data:
    row = []
    for char in line.strip():
        row.append(int(char))

    costs.append(row)

newnodes = []

for i in range(len(costs) * 5):
    newrow = []
    for j in range(len(costs[i % len(costs)]) * 5):
        x = i % len(costs)
        y = j % len(costs[x])
        n = i // len(costs) + j // len(costs)
        newrow.append(Node(inc(costs[x][y], n)))
    newnodes.append(newrow)

for i in range(len(newnodes)):
    for j in range(len(newnodes[i])):
        if (i - 1) >= 0:
            newnodes[i][j].addneighbor(newnodes[i - 1][j])
        if (j - 1) >= 0:
            newnodes[i][j].addneighbor(newnodes[i][j - 1])
        if (i + 1) < len(newnodes):
            newnodes[i][j].addneighbor(newnodes[i + 1][j])
        if (j + 1) < len(newnodes[0]):
            newnodes[i][j].addneighbor(newnodes[i][j + 1])

new_start = newnodes[0][0]
new_end = newnodes[len(newnodes) - 1][len(newnodes) - 1]
dijkstra(new_start)
print(new_end.distance)