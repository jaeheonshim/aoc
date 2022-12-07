import pathlib
import sys
import re

def parse(puzzle_input):
    return puzzle_input

def part1(data):
    for i in range(4, len(data)):
        if len(set(data[i - 4:i])) == len(data[i - 4:i]):
            return i

def part2(data):
    for i in range(14, len(data)):
        if len(set(data[i - 14:i])) == len(data[i - 14:i]):
            return i

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