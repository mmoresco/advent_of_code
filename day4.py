from util import *

def parse_pair(assignment):
    def parse_range(r):
        start, end = map(int, r.strip().split('-'))
        return set(range(start, end + 1))

    first, second = assignment.split(',')
    return parse_range(first), parse_range(second)

def fully_contains(first, second):
    return first.issubset(second) or second.issubset(first)

def overlaps(first, second):
    return not first.isdisjoint(second)

def count_condition(assignments, condition):
    return sum([condition(*parse_pair(a)) for a in assignments])

test_input = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
        ] 

# PART 1
assert count_condition(test_input, fully_contains) == 2
print("Part 1:", count_condition(Input(4), fully_contains))

# PART 2
assert count_condition(test_input, overlaps) == 4
print("Part 2:", count_condition(Input(4), overlaps))
