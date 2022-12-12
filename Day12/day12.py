# AoC 2021
# Day 12
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 31
PUZZLE_2_TEST_RESULT = 29

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


def get_dist_matrix(input):
    start_x = start_y = end_x = end_y = 0
    rows = len(input)
    cols = len(input[0])
    gr = [[0] * (rows * cols) for _ in range(rows * cols)]

    for y in range(len(input)):
        for x in range(cols):
            if input[y][x] == "S":
                start_x, start_y = x, y
            elif input[y][x] == "E":
                end_x, end_y = x, y
            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + dx in range(cols) and y + dy in range(rows)):
                    if input[y][x] == "S":
                        if input[y + dy][x + dx] in ["a", "b"]:
                            gr[y * cols + x][(y + dy) * cols + (x + dx)] = 1
                    elif input[y + dy][x + dx] == "E":
                        if input[y][x] in ["y", "z"]:
                            gr[y * cols + x][(y + dy) * cols + (x + dx)] = 1
                    elif (ord(input[y + dy][x + dx]) - ord(input[y][x]) <= 1):
                        gr[y * cols + x][(y + dy) * cols + (x + dx)] = 1

    graph = csr_matrix(gr)
    dist_matrix = dijkstra(csgraph=graph, directed=True)
    return dist_matrix, start_y * cols + start_x, end_y * cols + end_x


def do_puzzle1(input):
    dist_matrix, start, end = get_dist_matrix(input)
    return dist_matrix[start][end]


def do_puzzle2(input):
    cols = len(input[0])
    dist_matrix, start, end = get_dist_matrix(input)
    start_points = [start]  # start point has elevation "a"
    for y in range(len(input)):
        for x in range(cols):
            if input[y][x] == "a":
                start_points.append(y * cols + x)

    return sorted([dist_matrix[s][end] for s in start_points])[0]


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle1(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    result = do_puzzle2(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
