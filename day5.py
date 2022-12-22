import itertools
from operator import itemgetter
from util import Input

def parse_stacks(raw):
    '''
		[D]    
	[N] [C]       ->  {'1': ['Z', 'N'], '2': ['M', 'C', 'D'], '3': ['P']}
	[Z] [M] [P]
	 1   2   3 
    '''

    lines = [[value for value in list(row) if value != ' '] for row in 
            zip(
                *[
                    [*line.replace('[', ' ').replace(']', ' ')] for line in raw[::-1]
                    ]
                )
            ]

    return {int(row[0]):row[1:] for row in lines if row}

def parse_instructions(raw):
    return [[int(v) for v in itemgetter(1, 3, 5)(line.split())] for line in raw]

def extract_parts(raw):
    return [list(group) for k, group in itertools.groupby(raw, lambda x: x == '') if not k]

def process_instructions(stacks, instructions):
    for count, start, end in instructions:
        for _ in range(count):
            stacks[end].append(
                    stacks[start].pop()
                    )
    return stacks

def process_instructions_CrateMover9001(stacks, instructions):
    for count, start, end in instructions:
        stacks[end].extend(stacks[start][-count:])
        del stacks[start][-count:]
    return stacks


def get_tops_of_stacks(stacks):
    res = []
    for i in range(len(stacks)):
        res.append(stacks[i+1][-1])

    return ''.join(res)

def part_1(inpt):
    raw_stacks, raw_instructions = extract_parts(inpt)
    stacks = parse_stacks(raw_stacks)
    instructions = parse_instructions(raw_instructions)
    process_instructions(stacks, instructions)
    return get_tops_of_stacks(stacks)

def part_2(inpt):
    raw_stacks, raw_instructions = extract_parts(inpt)
    stacks = parse_stacks(raw_stacks)
    instructions = parse_instructions(raw_instructions)
    process_instructions_CrateMover9001(stacks, instructions)
    return get_tops_of_stacks(stacks)

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split('\n')

real_input = Input(5).read().splitlines()

assert part_1(test_input) == 'CMZ'
print("Part 1:", part_1(real_input))

assert part_2(test_input) == 'MCD'
print("Part 2:", part_2(real_input))

