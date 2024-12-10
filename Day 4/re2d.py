import contextlib


def findall(pattern, string, rotate=False):
    """Find all two-dimensional matches of the pattern in the string."""
    pattern_grid = [list(line) for line in pattern.strip().split("\n")]
    grid = [list(line) for line in string.strip().split("\n")]
    if not rotate:
        return _findall(pattern_grid, grid)
    matches = []
    for i in range(4):
        matches.extend([(x,y,i) for (x,y) in _findall(pattern_grid, grid)])
        pattern_grid = _rotate(pattern_grid)

    return matches

def _findall(pattern_grid, grid):
    matches = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            match = True
            with contextlib.suppress(IndexError):
                for i in range(len(pattern_grid)):
                    for j in range(len(pattern_grid[0])):
                        if pattern_grid[i][j] == ".":
                            continue

                        c = "." if pattern_grid[i][j] == "\\." else pattern_grid[i][j]

                        if grid[x+i][y+j] != c:
                            match = False
                            break

                if match:
                    matches.append((x,y))

    return matches

def _transpose(grid):
    """Transpose the grid."""
    return [[grid[x][y] for x in range(len(grid))] for y in range(len(grid[0]))]

def _flip(grid):
    """Flip the grid horizontally."""
    return [[grid[x][y] for y in reversed(range(len(grid[0])))] for x in range(len(grid))]

def _rotate(grid):
    """Rotate the grid counter-clockwise."""
    return _transpose(_flip(grid))