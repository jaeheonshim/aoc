import pathlib
import sys
import re

class Node:
    def __init__(self):
        self.parent = None
        self.children = {}
        self.fileAmount = 0

def parse(puzzle_input):
    fs = {}
    parent = Node()
    current = parent

    n = 0
    lines = puzzle_input.split("\n")

    while n < len(lines):
        line = lines[n].split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current = parent
                elif line[2] == "..":
                    current = current.parent
                else:
                    if line[2] in current.children:
                        current = current.children[line[2]]
                    else:
                        new = Node()
                        new.parent = current
                        current.children[line[2]] = new
                        current = new
        else:
            if line[0] == "dir":
                if line[1] not in current.children:
                    current.children[line[1]] = Node()
                    current.children[line[1]].parent = current
            else:
                current.fileAmount += int(line[0])

        n += 1
    
    return parent

def calculateDirSums(node, sums):
    total = node.fileAmount
    for child in node.children.values():
        total += calculateDirSums(child, sums)

    sums.append(total)
    return total

def calculateTotalSize(node):
    total = node.fileAmount
    for child in node.children.values():
        total += calculateTotalSize(child)
    return total

def part1(data):
    sums = []
    calculateDirSums(data, sums)
    
    return sum(filter(lambda x: x <= 100000, sums))

def part2(data):
    sums = []
    calculateDirSums(data, sums)
    unused = 70000000 - calculateTotalSize(data)
    
    for dirSize in sorted(sums):
        if unused + dirSize >= 30000000:
            return dirSize

def solve(puzzle_input):
    solution1 = part1(parse(puzzle_input))
    solution2 = part2(parse(puzzle_input))

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))