import pathlib
import sys

def parse(puzzle_input):
    return list(map(int, puzzle_input.split(",")))

def process(data):
    for i in range(0, len(data), 4):
        if data[i] == 99: break
        elif data[i] == 1:
            added = data[data[i + 1]] + data[data[i + 2]]
            data[data[i+3]] = added
        elif data[i] == 2:
            mult = data[data[i + 1]] * data[data[i + 2]]
            data[data[i+3]] = mult
    
    return data[0]

def part1(data):
    data[1] = 12
    data[2] = 2
    return process(data)

def part2(data):
    for i in range(100):
        for j in range(100):
            d = data.copy()
            d[1] = i
            d[2] = j
            if process(d) == 19690720:
                return 100 * i + j

def solve(puzzle_input):
    solution1 = part1(parse(puzzle_input))
    solution2 = part2(parse(puzzle_input))

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))