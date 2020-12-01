def read_numbers(filename):
    with open(filename) as f:
        return map(int, f)


records = read_numbers("input.txt")

# ---- PART ONE ----
# jeez I feel this is poor:


def result1():
    for val1 in records:
        for val2 in records:
            if val1 + val2 == 2020:
                print(val1 * val2)
                return


# ---- PART TWO ----
# my god


def result2():
    for val1 in records:
        for val2 in records:
            for val3 in records:
                if val1 + val2 + val3 == 2020:
                    print(val1 * val2 * val3)
                    return


result1()
result2()
