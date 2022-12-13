# AoC 2021
# Day 13
#
# Dr Bob, Tech Team, DigitalUK
import functools

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 13
PUZZLE_2_TEST_RESULT = 140


def parse_list(aList, line, index=1):
    val = None

    while True:
        if line[index] == "[":
            newList = []
            aList.append(newList)
            index = parse_list(newList, line, index + 1)
            if line[index] == ",":
                index += 1

        if (line[index].isdigit()):
            if val is None:
                val = 0
            val = val * 10 + int(line[index])
        else:
            if val is not None:
                aList.append(val)
            val = None

        if line[index] == "]":
            break

        index += 1

    return index + 1


def compare(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return -1 if a < b else 1 if a > b else 0
        else:
            return compare([a], b)
    else:
        if isinstance(b, int):
            return compare(a, [b])
        else:
            pass  # do list comparison here
            for i, item_a in enumerate(a):
                if i >= len(b):
                    return 1
                test = compare(a[i], b[i])
                if test != 0:
                    return test
            if len(b) > len(a):
                return -1
            else:
                return 0


def do_puzzle1(input):
    packets = []
    pairs = [(pair.split("\n")[0], pair.split("\n")[1]) for pair in "\n".join(input).split("\n\n")]
    for (left, right) in pairs:
        left_packet = []
        right_packet = []
        parse_list(left_packet, left)
        parse_list(right_packet, right)
        packets.append((left_packet, right_packet))

    ordering = [compare(a, b) for (a, b) in packets]
    sums = (i + 1 if v == -1 else 0 for i, v in enumerate(ordering))
    return sum(sums)


def do_puzzle2(input):
    input.extend(["[[2]]", "[[6]]"])
    packets = []
    for i in input:
        if len(i) > 0:
            packet = []
            parse_list(packet, i)
            packets.append(packet)

    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


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
