import pathlib
import sys
import re

def parse(puzzle_input):
    return [[int(x) for x in line] for line in puzzle_input.strip().split("\n")]

def part1(data):
    visibility = [[False] * len(data) for x in data]

    # check rows
    for i in range(len(data)):
        f = 0
        b = len(data) - 1
        f_height = -1
        b_height = -1

        while f < len(data) and b >= 0:
            if data[i][f] > f_height:
                visibility[i][f] = True
            if data[i][b] > b_height:
                visibility[i][b] = True

            f_height = max(data[i][f], f_height)
            b_height = max(data[i][b], b_height)

            f += 1
            b -= 1

    # check columns
    for i in range(len(data)):
        f = 0
        b = len(data) - 1
        f_height = -1
        b_height = -1

        while f < len(data) and b >= 0:
            if data[f][i] > f_height:
                visibility[f][i] = True
            if data[b][i] > b_height:
                visibility[b][i] = True

            f_height = max(data[f][i], f_height)
            b_height = max(data[b][i], b_height)

            f += 1
            b -= 1

    return sum(map(lambda x: sum(map(int, x)), visibility))

def calc_scenic(data, r, c):
    height = data[r][c]
    s1 = s2 = s3 = s4 = 1
    while r - s1 >= 0 and data[r - s1][c] < height:
        s1 += 1
    while r + s2 < len(data) and data[r + s2][c] < height:
        s2 += 1
    while c - s3 >= 0 and data[r][c - s3] < height:
        s3 += 1
    while c + s4 < len(data) and data[r][c + s4] < height:
        s4 += 1

    return min(s1, r) * min(s2, len(data) - r - 1) * min(s3, c) * min(s4, len(data) - c - 1)

def part2(data):
    scenic_data = []

    for r in range(len(data)):
        scenic_data.append([])
        for c in range(len(data)):
            scenic_data[r].append(calc_scenic(data, r, c))

    return max(map(max, scenic_data))

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