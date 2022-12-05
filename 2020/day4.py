# 12:35

import pathlib
import sys
import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def parse(puzzle_input):
    return [re.split(" |\n", x) for x in puzzle_input.split("\n\n")]

def part1(data):
    c = 0
    for person in data:
        found = set()
        for entry in person:
            for r in required:
                if r in entry: found.add(r)
        if len(found) == len(required):
            c += 1

    return c

def check_pass_valid(d):
    found = set()
    for entry in d:
        for r in required:
            if r in entry: found.add(r)
    if len(found) != len(required):
        return False
    
    for entry in d:
        parts = entry.split(":")
        if parts[0] == "byr":
            if not (1920 <= int(parts[1]) <= 2002): return False
        if parts[0] == "iyr":
            if not (2010 <= int(parts[1]) <= 2020): return False
        if parts[0] == "eyr":
            if not (2020 <= int(parts[1]) <= 2030): return False
        if parts[0] == "hgt":
            if parts[1][-2:] == "cm":
                if not (150 <= int(parts[1][:-2]) <= 193): return False
            elif parts[1][-2:] == "in":
                if not (59 <= int(parts[1][:-2]) <= 76): return False
            else: return False
        if parts[0] == "hcl":
            if parts[1][0] != "#" or len(parts[1]) - 1 != 6: return False
        if parts[0] == "ecl":
            if parts[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
        if parts[0] == "pid":
            try:
                int(parts[1])
                if(len(parts[1]) != 9): return False
            except: return False

    return True

def part2(data):
    c = 0
    for p in data:
        if check_pass_valid(p): c += 1

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