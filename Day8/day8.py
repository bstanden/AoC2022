# AoC 2021
# Day 8
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 21
PUZZLE_2_TEST_RESULT = 8


def do_puzzle1(input):
    left_right = set()
    up_down = set()
    for y in range(0, len(input)):
        max_height = -1
        for x in range(len(input[0])):
            z = int(input[y][x])
            if z > max_height:
                max_height = z
                left_right.add((x, y))

        max_height = -1
        for x in reversed(range(len(input[0]))):
            if (x, y) in left_right:
                break;
            z = int(input[y][x])
            if z > max_height:
                max_height = z
                left_right.add((x, y))

    for x in range(0, len(input[0])):
        max_height = -1
        for y in range(len(input)):
            z = int(input[y][x])
            if z > max_height:
                max_height = z
                up_down.add((x, y))

        max_height = -1
        for y in reversed(range(len(input))):
            if (x, y) in up_down:
                break;
            z = int(input[y][x])
            if z > max_height:
                max_height = z
                up_down.add((x, y))

    return len(left_right.union(up_down))


def do_puzzle2(input):
    max = 0
    for x in range(1, len(input[0]) - 1):
        for y in range(1, len(input) - 1):

            r_dist = 0
            for d in range(x + 1, len(input[0])):
                r_dist = r_dist + 1
                if int(input[y][d]) >= int(input[y][x]):
                    break

            l_dist = 0
            for d in reversed(range(0, x)):
                l_dist = l_dist + 1
                if int(input[y][d]) >= int(input[y][x]):
                    break

            d_dist = 0
            for d in range(y + 1, len(input)):
                d_dist = d_dist + 1
                if int(input[d][x]) >= int(input[y][x]):
                    break

            u_dist = 0
            for d in reversed(range(0, y)):
                u_dist = u_dist + 1
                if int(input[d][x]) >= int(input[y][x]):
                    break

            sight = l_dist * r_dist * u_dist * d_dist

            if sight > max:
                max = sight

    return max


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
