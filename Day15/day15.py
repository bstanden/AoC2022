# AoC 2022
# Day 15
#
# Dr Bob, Tech Team, DigitalUK


INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_ROW = 10
PUZZLE_1_TEST_RESULT = 26
PUZZLE_1_ROW = 2000000

PUZZLE_2_TEST_MAX_COORD = 20
PUZZLE_2_TEST_RESULT = 56000011
PUZZLE_2_MAX_COORD = 4000000


class Sensor:
    def __init__(self, coord, b_coord):
        self.coord = coord
        self.b_coord = b_coord

    def extent(self, y):
        (s_x, s_y) = self.coord
        (b_x, b_y) = self.b_coord

        r = abs(s_x - b_x) + abs(s_y - b_y)

        dist = abs(y - s_y)
        if dist > r:
            return range(0)
        else:
            return range(s_x - (r - dist), s_x + (r - dist) + 1)

    def min_max(self, p, limit):
        (s_x, s_y) = self.coord
        (b_x, b_y) = self.b_coord

        x_range = y_range = None

        r = abs(s_x - b_x) + abs(s_y - b_y)

        y_dist = abs(p - s_y)
        if y_dist <= r:
            x_range = rlimit((s_x - (r - y_dist), s_x + (r - y_dist)), limit)

        x_dist = abs(p - s_x)
        if x_dist <= r:
            y_range = rlimit((s_y - (r - x_dist), s_y + (r - x_dist)), limit)

        return x_range, y_range


def rlimit(r, limit):
    (r_min, r_max) = r
    r_min = 0 if r_min < 0 else limit if r_min > limit else r_min
    r_max = 0 if r_max < 0 else limit if r_max > limit else r_max
    return r_min, r_max


def get_sensors(input):
    sensors = []
    for i in input:
        toks = i.split(" ")
        sensors.append(Sensor((int(toks[2].split("=")[1][:-1]), int(toks[3].split("=")[1][:-1])),
                              (int(toks[8].split("=")[1][:-1]), int(toks[9].split("=")[1]))))
    return sensors


def unify(a, b):
    a_min, a_max = a
    b_min, b_max = b

    if (a_max >= b_min and a_min <= b_max) or (a_max == b_min - 1 or b_max == a_min - 1):  # overlap or adjacent
        return min(a_min, b_min), max(a_max, b_max)  # return union of both
    else:
        return None


def range_complete(limits, max_coord):
    r_limits = [l for l in limits if l is not None]
    orig_len = len(r_limits)
    if not orig_len:
        return None

    while True:
        if len(r_limits) == 1:
            # only one item left. Likely complete range unles part of solution is 0 or max_coord
            return r_limits[0] == (0, max_coord)

        lim = r_limits.pop(0)
        for i, i_lim in enumerate(r_limits):
            u_lim = unify(lim, i_lim)
            if u_lim is not None:  # replace both candidates with combined limit
                r_limits.pop(i)
                r_limits.append(u_lim)
        if len(r_limits) == orig_len:
            return True  # list will no longer combine, but more than one limit. Beacon must be on this line.


def do_puzzle1(input, test_row):
    sensors = get_sensors(input)
    range = set()
    for s in sensors:
        for i in s.extent(test_row):
            if (i, test_row) not in [s.b_coord for s in sensors]:
                range.add(i)
    return len(range)


def do_puzzle2(input, max_coord):
    sensors = get_sensors(input)
    h_value = v_value = None
    for i in range(max_coord):
        h_limits, v_limits = zip(*[s.min_max(i, max_coord) for s in sensors])
        if not v_value:
            v_value = i if not range_complete(h_limits, max_coord) else None
        if not h_value:
            h_value = i if not range_complete(v_limits, max_coord) else None
        if h_value and v_value:
            break
    return h_value * 4000000 + v_value


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle1(read_file(INPUT_FILE_TEST), PUZZLE_1_TEST_ROW)
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE), PUZZLE_1_ROW)
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    result = do_puzzle2(read_file(INPUT_FILE_TEST), PUZZLE_2_TEST_MAX_COORD)
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE), PUZZLE_2_MAX_COORD)
    print(f"puzzle2 result: {result}")
