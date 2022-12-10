# AoC 2021
# Day 10
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_TEST_RESULT = 13140

SCREEN_WIDTH = 40


def do_puzzle(input):
    instructions = enumerate([op for line in input for op in line.split()])
    x = 1
    output = 0
    for i, op in instructions:
        print("█" if abs((i % SCREEN_WIDTH) - x) <= 1 else " ", end="" if (i + 1) % SCREEN_WIDTH else None)

        if not (i + 21) % SCREEN_WIDTH:
            output += (i + 1) * x
        if not op.isalpha():
            x += int(op)
    print()
    return output


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")
