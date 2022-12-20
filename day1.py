from util import *

def parse_food(lines):
    return [[int(meal) for meal in elf.strip().split('\n')] for elf in lines.split('\n\n')]

def most_cals_with_top_n_elves(elves, n=1):
    return sum(MaxN([sum(elf) for elf in elves], n))

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

# PART 1
assert parse_food(test_input) == [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
assert most_cals_with_top_n_elves(parse_food(test_input)) == 24000

elves = parse_food(Input(1).read())
print("Part 1:", most_cals_with_top_n_elves(elves))

# PART 2
assert most_cals_with_top_n_elves(parse_food(test_input), 3) == 45000
print("Part 2:", most_cals_with_top_n_elves(elves, 3))
