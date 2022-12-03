import pathlib
import sys

def calc_fuel(x):
    fuel = (x // 3) - 2
    if max(fuel, 0) == 0: return 0
    return fuel + calc_fuel(fuel)

def parse(puzzle_input):
    return [int(x) for x in puzzle_input.split("\n")]

def part1(data):
    s = 0
    for i in data:
        s += (i // 3) - 2

    return s

def part2(data):
    s = 0
    for i in data:
        s += calc_fuel(i)

    return s

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