def move(start, x):
    return (start + x) % 31


def is_tree(x, line):
    if line[x] == '#':
        return True
    return False


def count(trees, x, skip):
    result = 0
    is_odd = True
    position = 0

    for line in trees:
        if is_odd:
            if is_tree(position, line):
                result += 1
            position = move(position, x)
        if skip:
            is_odd = not is_odd

    return result


tree_map = open('input.txt', 'r').readlines()
pos_x = 0

# ---- PART ONE ----

answer = count(tree_map, 3, False)
print answer

# ---- PART TWO ----

a = count(tree_map, 1, False)
b = count(tree_map, 3, False)
c = count(tree_map, 5, False)
d = count(tree_map, 7, False)
e = count(tree_map, 1, True)

answer = a * b * c * d * e
print answer

