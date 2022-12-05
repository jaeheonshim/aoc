import pathlib
import sys

def parse_line(line):
    parts = line.split(" ")
    min, max = parts[0].split("-")
    c = parts[1][:-1]
    pwd = parts[-1]

    return (min, max, c, pwd)

def parse(puzzle_input):
    return list(map(parse_line, puzzle_input.split("\n")))

def part1(data):
    s = 0
    for d in data:
        if int(d[1]) >= d[3].count(d[2]) >= int(d[0]): s += 1

    return s

def part2(data):
    s = 0
    for d in data:
        if (d[3][int(d[0]) - 1] == d[2]) != (d[3][int(d[1]) - 1] == d[2]): s += 1

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