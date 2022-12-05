# AoC 2022
# Day 4
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 2
PUZZLE_2_TEST_RESULT = 4


def get_pairs(input):
    pairs = []
    for i in input:
        left, right = i.split(',')
        min, max = left.split('-')
        a = set(range(int(min), int(max) + 1))
        min, max = right.split('-')
        b = set(range(int(min), int(max) + 1))
        pairs.append((a, b))
    return pairs


def do_puzzle1(input):
    pairs = get_pairs(input)
    count = 0
    for (a, b) in pairs:
        if a.issubset(b) or b.issubset(a):
            count = count + 1
    return count


def do_puzzle2(input):
    pairs = get_pairs(input)
    count = 0
    for (a, b) in pairs:
        if len(a.intersection(b)):
            count = count + 1
    return count


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
