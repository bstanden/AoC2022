# AoC 2022
# Day 14
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 24
PUZZLE_2_TEST_RESULT = 93


def parse_rocks(input, rocks):
    for i in input:
        coords = [(int(coords.split(",")[0]), int(coords.split(",")[1])) for coords in i.split(" ")[::2]]
        for n in range(len(coords) - 1):
            (a_x, a_y) = coords[n]
            (b_x, b_y) = coords[n + 1]
            if a_x == b_x:
                if a_y > b_y:
                    for y in range(b_y, a_y + 1):
                        rocks.add((a_x, y))
                else:
                    for y in range(a_y, b_y + 1):
                        rocks.add((a_x, y))
            elif a_y == b_y:
                if a_x > b_x:
                    for x in range(b_x, a_x + 1):
                        rocks.add((x, a_y))
                else:
                    for x in range(a_x, b_x + 1):
                        rocks.add((x, a_y))


def get_new_grain(rocks, grains, base, coord=(500, 0), abyss=True):
    while True:
        (x, y) = coord
        if abyss and y == base:
            break
        elif (x, y + 1) not in rocks and (x, y + 1) not in grains:
            if not abyss and y + 1 == base + 2:
                rocks.add((x, y + 1))
                break
            else:
                coord = (x, y + 1)
        elif (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in grains:
            if not abyss and y + 1 == base + 2:
                rocks.add((x - 1, y + 1))
                break
            else:
                coord = (x - 1, y + 1)
        elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in grains:
            if not abyss and y + 1 == base + 2:
                rocks.add((x + 1, y + 1))
                break
            else:
                coord = (x + 1, y + 1)
        else:
            break

    return coord


def do_puzzle1(input):
    rocks = set()
    parse_rocks(input, rocks)
    base = max([y for (x, y) in rocks])

    grains = set()
    while True:
        new_grain = get_new_grain(rocks, grains, base)
        (x, y) = new_grain
        if y == base:
            break
        grains.add(new_grain)

    return len(grains)


def do_puzzle2(input):
    rocks = set()
    parse_rocks(input, rocks)
    base = max([y for (x, y) in rocks])
    grains = set()

    while True:
        new_grain = get_new_grain(rocks, grains, base, abyss=False)
        grains.add(new_grain)
        if new_grain == (500, 0):
            break

    return len(grains)


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
