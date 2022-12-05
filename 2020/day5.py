# 11:51

import pathlib
import sys
import re

def get_seat_id(s):
    a = 0
    b = 127
    
    for c in s[:-4]:
        if c == "F":
            b = a + (b - a) // 2
        elif c == "B":
            a = b - ((b - a) // 2)

    if s[-4] == "F":
        se = min(a, b)
    else:
        se = max(a, b)

    a = 0
    b = 7
    
    for c in s[-3:-1]:
        if c == "L":
            b = a + (b - a) // 2
        elif c == "R":
            a = b - ((b - a) // 2)

    if s[-1] == "L":
        c = min(a, b)
    else:
        c = max(a, b)

    return se * 8 + c

def parse(puzzle_input):
    return puzzle_input.split("\n")

def part1(data):
    ids = [get_seat_id(x) for x in data]
    return max(ids)

def part2(data):
    data.sort()
    for i in range(1, len(data)):
        if get_seat_id(data[i]) - get_seat_id(data[i - 1]) > 1:
            return get_seat_id(data[i - 1]) + 1

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