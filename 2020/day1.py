# 2:52

import pathlib
import sys

def parse(puzzle_input):
    return list(map(int, puzzle_input.split("\n")))

def part1(data):
    found = set()

    for i in data:
        if (2020 - i) in found:
            return i * (2020 - i)
        else:
            found.add(i)

    return None

def part2(data):
    found = set()

    for i in range(len(data)):
        for j in range(i, len(data)):
            if (2020 - data[i] - data[j]) in found:
                return data[i] * data[j] * (2020 - data[i] - data[j])
            else:
                found.add(data[j])
        found.add(data[i])

    return None

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