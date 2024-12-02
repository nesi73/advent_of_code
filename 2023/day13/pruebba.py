# Day 13 - Point of Incidence

from enum import Enum

class Mode(Enum):
    ROW = "row"
    COLUMN = "column"

def is_perfect_reflection(prev, next, pattern, mode):
    if mode == Mode.ROW:
        while prev >= 0 and next < len(pattern):
            if pattern[prev] != pattern[next]:
                return False
            prev -= 1
            next += 1

        return True

    elif mode == Mode.COLUMN:
        while prev >= 0 and next < len(pattern[0]):
            for i in range(len(pattern)):
                if pattern[i][prev] != pattern[i][next]:
                    return False
            prev -= 1
            next += 1

        return True

    raise Exception("Invalid mode")

def find_point_of_reflection(pattern, mode):
    if mode == Mode.ROW:
        for i in range(1, len(pattern)):
            if pattern[i-1] == pattern[i]:
                if is_perfect_reflection(i-1, i, pattern, Mode.ROW):
                    return i

    if mode == Mode.COLUMN:
        for j in range(1, len(pattern[0])):
            prev_col, next_col = [], []
            for i in range(0, len(pattern)):
                prev_col.append(pattern[i][j-1])
                next_col.append(pattern[i][j])
            if prev_col == next_col:
                if is_perfect_reflection(j-1, j, pattern, Mode.COLUMN):
                    return j

def analyze_pattern(pattern):
    pattern_grid = [list(row) for row in pattern.strip().split("\n")]

    # Find the point of reflection row by row
    point = find_point_of_reflection(pattern_grid, Mode.ROW)
    if point:
        return point * 100

    # Find the point of reflection column by column
    point = find_point_of_reflection(pattern_grid, Mode.COLUMN)
    if point:
        return point

    raise Exception("No point of reflection found")

def summarize_patterns(patterns):
    sum = 0
    for pattern in patterns.split("\n\n"):
        sum += analyze_pattern(pattern)

    return sum

def part_one():
    with open("input.txt", "r") as f:
        patterns = f.read()
    sum = summarize_patterns(patterns)

    print(f"❗️ Summarizing all patterns in Part 1: {sum}")

def test_summarize_patterns():
    patterns = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    sum = summarize_patterns(patterns)
    assert sum == 405, f"Expected 405, got {sum}"
    print("✅ summarize_pattern passed")

if __name__ == "__main__":
    test_summarize_patterns()
    part_one()