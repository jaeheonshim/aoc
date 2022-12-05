import pathlib
import sys
import re

def parse(puzzle_input):
    return list(map(lambda x: x.split(","), puzzle_input.split("\n")))

def part1(data):
    c = 0
    for entry in data:
        (r1, r1f) = list(map(int, entry[0].split("-")))
        (r2, r2f) = list(map(int, entry[1].split("-")))

        if r2 >= r1 and r2f <= r1f or r1 >= r2 and r1f <= r2f:
            c += 1

    return c

def part2(data):
    c = 0
    for entry in data:
        (r1, r1f) = list(map(int, entry[0].split("-")))
        (r2, r2f) = list(map(int, entry[1].split("-")))

        if r2 >= r1 and r2 <= r1f or r1 >= r2 and r1 <= r2f:
            c += 1
    return c

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