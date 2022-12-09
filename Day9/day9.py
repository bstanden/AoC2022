# AoC 2021
# Day 9
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE_TEST2 = "input_test2.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 13
PUZZLE_2_TEST_RESULT = 1
PUZZLE_2_TEST2_RESULT = 36


def get_tail_movements(input, nodes):
    rope = [(0, 0)] * nodes
    visits = set()
    delta = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    for i in input:
        toks = i.split(" ")
        dir = toks[0]
        count = int(toks[1])
        for n in range(count):
            rope[0] = tuple(map(lambda i, j: i + j, rope[0], delta[dir]))
            for p in range(nodes - 1):
                (d_x, d_y) = tuple(map(lambda i, j: i - j, rope[p], rope[p + 1]))
                (head_x, head_y) = rope[p]
                (tail_x, tail_y) = rope[p + 1]
                if abs(d_x) == 2:
                    tail_x = tail_x + d_x // 2
                    if abs(d_y) == 2:  # because diagonal motion is possible where > 2 nodes on rope
                        tail_y = tail_y + d_y // 2
                    else:
                        tail_y = head_y

                elif abs(d_y) == 2:
                    tail_y = tail_y + d_y // 2
                    tail_x = head_x

                rope[p + 1] = (tail_x, tail_y)

            visits.add(rope[-1])
    return len(visits)


def do_puzzle1(input):
    return get_tail_movements(input, 2)


def do_puzzle2(input):
    return get_tail_movements(input, 10)


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

    # puzzle 2 example 2
    result = do_puzzle2(read_file(INPUT_FILE_TEST2))
    assert result == PUZZLE_2_TEST2_RESULT, f"Failed Puzzle 2 assertion 2: expected {PUZZLE_2_TEST2_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
