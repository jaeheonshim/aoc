import pathlib
import sys

def parse(puzzle_input):
    l = []
    for line in puzzle_input.split("\n\n"):
        l.append(sum([int(x) for x in line.split("\n")]))

    return l

def part1(data):
    return max(data)


def part2(data):
    s = sorted(data)
    return s[-1] + s[-2] + s[-3]

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
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