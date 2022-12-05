# 4:17

import pathlib
import sys

def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    data = []
    for line in lines:
        data.append([1 if x == "#" else 0 for x in line])
    
    return data

def part1(data):
    cnt = 0
    x = 0
    y = 0
    while y < len(data):
        if data[y][x] == 1: cnt += 1
        x += 3
        y += 1
        if x >= len(data[0]): x %= len(data[0])

    return cnt

def checkslope(data, dx, dy):
    cnt = 0
    x = 0
    y = 0
    while y < len(data):
        if data[y][x] == 1: cnt += 1
        x += dx
        y += dy
        if x >= len(data[0]): x %= len(data[0])

    return cnt

def part2(data):
    return checkslope(data, 1, 1) * checkslope(data, 3, 1) * checkslope(data, 5, 1) * checkslope(data, 7, 1) * checkslope(data, 1, 2)

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))