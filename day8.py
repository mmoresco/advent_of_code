import util
import math

def visible(grid, x, y):
    value = grid[y][x]
    row = grid[y]
    column = [row[x] for row in grid]

    return not all([
        [v for v in row[0:x] if v >= value],
        [v for v in row[x+1:] if v >= value],
        [v for v in column[0:y] if v >= value],
        [v for v in column[y+1:] if v >= value]
        ])

def scenic_score(grid, x, y):
    def blocking_tree(trees):
        if not trees:
            return 0
        return next(i+1 for i, v in enumerate(trees) if v >= value or i == len(trees) - 1)

    value = grid[y][x]
    row = grid[y]
    column = [row[x] for row in grid]

    return math.prod([blocking_tree(list(reversed(row[0:x]))),
            blocking_tree(row[x+1:]),
            blocking_tree(list(reversed(column[0:y]))),
            blocking_tree(column[y+1:])])

def find_visible(grid):
    return [(x, y) for y, row in enumerate(grid) for x, column in enumerate(row) if visible(grid, x, y)]

def find_highest_scenic_score(grid):
    return max([scenic_score(grid, x, y) for y, row in enumerate(grid) for x, column in enumerate(row)])


test_input = '''30373
25512
65332
33549
35390'''

test_grid = util.Grid(test_input)
assert visible(test_grid, 3, 1) == False
assert len(find_visible(test_grid)) == 21
assert scenic_score(test_grid, 2, 1) == 4
assert scenic_score(test_grid, 2, 3) == 8

grid = util.Grid(util.Input(8).read())
print("Part 1:", len(find_visible(grid)))
print("Part 2:", find_highest_scenic_score(grid))
