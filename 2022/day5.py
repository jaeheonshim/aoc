import pathlib
import sys
import re

def parse(puzzle_input):
    i = 0
    lines = puzzle_input.split("\n")

    groups = (len(lines[0]) + 1) // 4

    stacks = [[] for x in range(groups)]
    while i < len(lines):
        line = lines[i]
        if '[' not in line: break

        for j in range(0, groups):
            if line[j * 4:j * 4 + 3][1] == ' ':continue
            stacks[j].append(line[j * 4:j * 4 + 3][1])
        i += 1
    
    i += 2

    cmds = []
    while i < len(lines):
        split = lines[i].split(" ")
        cmds.append((int(split[1]), int(split[3]), int(split[5])))
        i += 1

    return stacks, cmds

def runcommand1(map, f, t, q):
    for i in range(q):
        map[t - 1].insert(0, map[f - 1].pop(0))

def runcommand2(map, f, t, q):
    s = list([map[f - 1].pop(0) for x in range(q)])
    map[t - 1] = s + map[t - 1]

def part1(data):
    stack, cmds = data
    for cmd in cmds:
        runcommand1(stack, cmd[1], cmd[2], cmd[0])

    for c in stack:
        print(c.pop(0), end = "")

    print()

def part2(data):
    stack, cmds = data
    for cmd in cmds:
        runcommand2(stack, cmd[1], cmd[2], cmd[0])

    for c in stack:
        print(c.pop(0), end = "")

    print()

    # Solutions are printed for this one

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