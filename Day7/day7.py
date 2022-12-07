# AoC 2021
# Day 7
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 95437
PUZZLE_2_TEST_RESULT = 24933642

FREE_SPACE_NEEDED = 30000000
DEVICE_SPACE = 70000000


def get_filesystem(input):
    filesystem = dict()
    path = [filesystem]

    for i in input:
        toks = i.split(" ")
        if toks[0] == "$":  # command
            if toks[1] == "cd":
                if toks[2] == "/":
                    path = [filesystem]
                elif toks[2] == "..":
                    path.pop()
                else:
                    path.append(path[-1][toks[2]])  # add named directory to end of path
        elif toks[0] == "dir":  # add directory to current point on path
            path[-1][toks[1]] = dict()
        else:  # file
            path[-1][toks[1]] = int(toks[0])  # add file to current point on path

    return filesystem


def size_filesystem(filesystem, size_list, max_size=None):
    size = 0
    for v in filesystem.values():
        if type(v) is int:
            size = size + v
        else:
            size = size + size_filesystem(v, size_list, max_size)

    if max_size is None or size <= max_size:
        size_list.append(size)
    return size


def do_puzzle1(input):
    filesystem = get_filesystem(input)
    size_list = []
    size_filesystem(filesystem, size_list, 100000)
    return sum(size_list)


def do_puzzle2(input):
    filesystem = get_filesystem(input)
    dir_list = []
    space_needed = FREE_SPACE_NEEDED - DEVICE_SPACE + size_filesystem(filesystem, dir_list)
    candidates = sorted([d for d in dir_list if d >= space_needed])
    return candidates[0]


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
