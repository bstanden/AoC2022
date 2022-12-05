# AoC 2022
# Day 2
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 15
PUZZLE_2_TEST_RESULT = 12

ROCK = 0
PAPER = 1
SCISSORS = 2


def do_puzzle1(input):
    strategy = [("ABC".find(i[0]), "XYZ".find(i[2])) for i in input]
    scores = []
    for (them, me) in strategy:
        score = me + 1
        if (me == ROCK and them == SCISSORS) or (me == PAPER and them == ROCK) or (me == SCISSORS and them == PAPER):
            score = score + 6
        elif them == me:
            score = score + 3
        scores.append(score)

    return sum(scores)


def do_puzzle2(input):
    strategy = [("ABC".find(i[0]), "XYZ".find(i[2])) for i in input]
    scores = []
    for (them, result) in strategy:
        if result == 0:
            if them == ROCK:
                me = SCISSORS
            elif them == PAPER:
                me = ROCK
            else:
                me = PAPER
        elif result == 1:
            me = them
        else:
            if them == ROCK:
                me = PAPER
            elif them == PAPER:
                me = SCISSORS
            else:
                me = ROCK
        score = me + 1 + (result * 3)

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
