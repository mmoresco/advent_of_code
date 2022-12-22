from collections import defaultdict

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

class Node:
    def __init__(self, name, parent, size=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size

    def print(self, indent=0):
        for _, v in self.children.items():
            print(' ' * indent, v.name, v.size)
            v.print(indent+2)

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

def process_commands(commands):
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


commands = parse_commands(test_input)

tree = process_commands(commands)
tree.print()

