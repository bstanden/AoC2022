# AoC 2022
# Day 5
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = "CMZ"
PUZZLE_2_TEST_RESULT = "MCD"


def parse_input(input):
    stacks = {}
    instructions = []
    for i in input:
        if "[" in i:
            num = len(i) // 4
            for n in range(0, num + 1):
                if not n in stacks:
                    stacks[n] = []
                if i[n * 4 + 1] != " ":
                    stacks[n].insert(0, i[n * 4 + 1])
        elif "m" in i:
            toks = i.split(" ")
            num = int(toks[1])
            src = int(toks[3]) - 1
            dst = int(toks[5]) - 1
            instructions.append((num, src, dst))

    return stacks, instructions


def do_puzzle1(input):
    stacks, instructions = parse_input(input)
    for (num, src, dst) in instructions:
        for n in range(0, num):
            stacks[dst].append(stacks[src].pop())

    return "".join([s.pop() for s in stacks.values()])


def do_puzzle2(input):
    stacks, instructions = parse_input(input)
    for (num, src, dst) in instructions:
        moves = [stacks[src].pop() for n in range(0, num)]
        moves.reverse()
        stacks[dst].extend(moves)

    return "".join([s.pop() for s in stacks.values()])


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.rstrip() for e in lines]  # in this test, leading whitespace is significant


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
