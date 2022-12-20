from util import *

def priority(item):
    return ord(item) - (38 if item.isupper() else 96)

def shared_item(sack):
    midpoint = len(sack)//2
    first, second = sack[:midpoint], sack[midpoint:]
    return set(first).intersection(set(second)).pop()

def sack_priorities(sacks):
    return sum([priority(shared_item(sack)) for sack in sacks])

def badge(group):
    return set.intersection(*[set(elf) for elf in group]).pop()

def badge_priorities(sacks):
    return sum([priority(badge(group)) for group in Chunks(sacks, 3)])

test_input = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

# PART 1
sacks = Input(3).read().splitlines()

assert sack_priorities(test_input) == 157
print ("Part 1:", sack_priorities(sacks)) 

# PART 2
assert badge_priorities(test_input) == 70
print("Part 2:", badge_priorities(sacks))


