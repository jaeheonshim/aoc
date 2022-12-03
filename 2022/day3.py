import pathlib
import sys

def get_priority(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

def parse(puzzle_input):
    return [x for x in puzzle_input.split("\n")]

def part1(data):
    s = 0
    for e in [(x[:len(x) // 2], x[len(x) // 2:]) for x in data]:
        pts = set()
        for c in e[1]:
            if c in e[0] and c not in pts:
                s += get_priority(c)
                pts.add(c)

    return s

def part2(data):
    s = 0

    for i in range(0, len(data), 3):
        e1 = data[i]
        e2 = data[i + 1]
        e3 = data[i + 2]

        for c in e1:
            if c in e2 and c in e3:
                s += get_priority(c)
                break
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