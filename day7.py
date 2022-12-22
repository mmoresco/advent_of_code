from collections import defaultdict
from util import Input

class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size

    def print(self, indent=0):
        for v in self.children.values():
            print(' ' * indent, v.name, v.size)
            v.print(indent+2)

    def total_size(self):
        return self.size + sum([v.total_size() for v in self.children.values()])

    def eligible_dirs(self, condition):
        ret = []
        if self.children and condition(self):
            ret.append(self)
        for v in self.children.values():
            ret.extend(v.eligible_dirs(condition))
        return ret

def build_file_tree(raw):
    def parse_commands(raw):
        res = []
        command_blocks = raw.split('$')
        for block in command_blocks:
            commands = block.strip().split('\n')

            inpt = commands[0].strip()
            output = [w.strip().split() for w in commands[1:]]
            words = inpt.split(' ')
            command = words[0]
            params = words[1:]
            
            if command:
                res.append((command, params, output))

        return res

    commands = parse_commands(raw)
    current_location = root = Node('/', None)

    for command, params, output in commands:
        if command == 'cd':
            name = params[0]
            if name == '..':
                current_location = current_location.parent
            else:
                if current_location.children.get(name) is None:
                    new_location = Node(name, current_location)
                    current_location.children[name] = new_location
                    current_location = new_location

        if command == 'ls':
            for res in output:
                if res[0] != 'dir':
                    size, name = res
                    current_location.children[name] = Node(name, current_location, int(size))

    return root

def candidate_sum(tree, n=100000):
    return sum([n.total_size() for n in tree.eligible_dirs(lambda x: x.total_size() <= n)])

def smallest_eligible_dir(tree):
    space_to_find = 30000000 - 70000000 + tree.total_size()
    return min([c.total_size() for c in tree.eligible_dirs(lambda x: x.total_size() >= space_to_find)])

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

tree = build_file_tree(test_input)
assert tree.total_size() == 48381165
assert [n.name for n in tree.eligible_dirs(lambda x: x.total_size() <= 100000)] == ['a', 'e']
assert candidate_sum(tree) == 95437
assert smallest_eligible_dir(tree) == 24933642

tree = build_file_tree(Input(7).read())
print("Part 1:", candidate_sum(tree))
print("Part 2:", smallest_eligible_dir(tree))

