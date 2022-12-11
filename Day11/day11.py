# AoC 2021
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 10605
PUZZLE_2_TEST_RESULT = 2713310158

NUM_ROUNDS_1 = 20
NUM_ROUNDS_2 = 10000


class Monkey:
    worry_limit = 1

    def __init__(self, input):
        self.activity = 0
        lines = input.split("\n")
        self.items = [int(i.strip()) for i in lines[1].split(":")[1].split(",")]

        toks = lines[2].split()
        self.operand = int(toks[-1]) if toks[-1].isnumeric() else None
        self.operation = toks[-2]

        self.test = int(lines[3].split()[-1])
        Monkey.worry_limit *= self.test

        self.trueAction = int(lines[4].split()[-1])
        self.falseAction = int(lines[5].split()[-1])

    def throw(self, monkeys, divide=True):
        self.activity += len(self.items)
        for i in self.items:
            op = self.operand if self.operand is not None else i
            worry = (i + op) % Monkey.worry_limit if self.operation == "+" else (i * op) % Monkey.worry_limit
            if divide:
                worry = worry // 3
            monkeys[self.falseAction if worry % self.test else self.trueAction].catch(worry)
        self.items = []

    def catch(self, i):
        self.items.append(i)


def do_puzzle(input, rounds, divide=True):
    monkeys = [Monkey(i) for i in "\n".join(input).split("\n\n")]
    for r in range(rounds):
        for m in monkeys:
            m.throw(monkeys, divide)

    activities = sorted([m.activity for m in monkeys], reverse=True)
    return activities[0] * activities[1]


def do_puzzle1(input):
    return do_puzzle(input, NUM_ROUNDS_1)


def do_puzzle2(input):
    return do_puzzle(input, NUM_ROUNDS_2, divide=False)


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
