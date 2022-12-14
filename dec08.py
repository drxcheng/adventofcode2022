SAMPLE = False

tree_heights_matrix = []

def is_visible(x, y):
    if x == 0 or x == len(tree_heights_matrix) - 1 or y == 0 or y == len(tree_heights_matrix[0]) - 1:
        return True

    height = tree_heights_matrix[x][y]

    # from top
    visible = True
    for i in range(0, x):
        if tree_heights_matrix[i][y] >= height:
            visible = False
            break
    if visible:
        return True

    # from bottom
    visible = True
    for i in range(x + 1, len(tree_heights_matrix)):
        if tree_heights_matrix[i][y] >= height:
            visible = False
            break
    if visible:
        return True

    # from left
    visible = True
    for i in range(0, y):
        if tree_heights_matrix[x][i] >= height:
            visible = False
            break
    if visible:
        return True

    # from right
    visible = True
    for i in range(y + 1, len(tree_heights_matrix[0])):
        if tree_heights_matrix[x][i] >= height:
            visible = False
            break
    if visible:
        return True

    return False

def get_scenic_score(x, y):
    if x == 0 or x == len(tree_heights_matrix) - 1 or y == 0 or y == len(tree_heights_matrix[0]) - 1:
        return 0

    height = tree_heights_matrix[x][y]

    # looking up
    score_up = 0
    for i in reversed(range(0, x)):
        score_up += 1
        if tree_heights_matrix[i][y] >= height:
            break

    # looking down
    score_down = 0
    for i in range(x + 1, len(tree_heights_matrix)):
        score_down += 1
        if tree_heights_matrix[i][y] >= height:
            break

    # looking left
    score_left = 0
    for i in reversed(range(0, y)):
        score_left += 1
        if tree_heights_matrix[x][i] >= height:
            break

    # looking right
    score_right = 0
    for i in range(y + 1, len(tree_heights_matrix[0])):
        score_right += 1
        if tree_heights_matrix[x][i] >= height:
            break

    return score_up * score_down * score_left * score_right


with open(f"dec08{'-sample' if SAMPLE else ''}.txt") as file:
    for line in file:
        tree_heights_matrix.append([int(c) for c in line.rstrip()])

    total_visible = 0
    max_scenic_score = 0
    for x in range(0, len(tree_heights_matrix)):
        for y in range(0, len(tree_heights_matrix[x])):
            total_visible += 1 if is_visible(x, y) else 0
            scenic_score = get_scenic_score(x, y)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(f'Part One: {total_visible}')
    print(f'Part Two: {max_scenic_score}')
