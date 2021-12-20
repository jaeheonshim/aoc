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