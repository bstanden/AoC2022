# AoC 2022
# Day 3
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 157
PUZZLE_2_TEST_RESULT = 70


def do_puzzle1(input):
    rucksacks = [(set(s[:len(s) // 2]), set(s[len(s) // 2:])) for s in input]

    scores = []
    for (a, b) in rucksacks:
        p = a.intersection(b)
        score = 0
        for e in p:
            score = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(e) + 1
        scores.append(score)

    return sum(scores)


def do_puzzle2(input):
    scores = []

    while len(input):
        a = set(input.pop(0))
        b = set(input.pop(0))
        c = set(input.pop(0))
        p = a.intersection(b, c)
        score = 0
        for e in p:
            score = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(e) + 1
        scores.append(score)

    return sum(scores)


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
