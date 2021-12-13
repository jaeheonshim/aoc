file = open("12.input")


path = {}
for line in file:
    parts = line.strip().split("-")
    path.setdefault(parts[0], []).append(parts[1])
    path.setdefault(parts[1], []).append(parts[0])

def travel(current, visited):
    if current == "end":
        return 1
    total = 0
    if current.islower():
        visited = visited + [current]
    for direction in path[current]:
        if direction not in visited and direction != "start":
            total += travel(direction, visited)

    return total

total = 0
total += travel("start", [])
print(total)

paths = set()
def travel2(current, current_path, single):
    if current == "end":
        paths.add(tuple(current_path))
        return
    if current.islower() and current in current_path and current != single:
        return
    elif current in current_path and current == single:
        single = ""
    current_path = current_path + [current]
    for direction in path[current]:
        if direction != "start":
            travel2(direction, current_path, single)

for key in path:
    if key.islower() and key != "start":
        travel2("start", [], key)
print(len(paths))