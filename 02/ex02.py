def parse(line):
    s = line.split(" ")
    a, b = s[0].split("-")
    letter = s[1][0]
    password = s[2][:-1]

    return a, b, letter, password


def validate1(let_min, let_max, letter, password):
    counter = password.count(letter)
    if int(let_min) <= counter <= int(let_max):
        return True
    return False


def validate2(a, b, letter, password):
    if password[int(a)-1] == letter and password[int(b)-1] != letter:
        return True
    if password[int(a) - 1] != letter and password[int(b) - 1] == letter:
        return True
    return False


# ---- PART ONE ----

answer = 0
lines = open('input.txt', 'r').readlines()

for line in lines:
    if validate1(*parse(line)):
        answer += 1

print ("Answer1: ", answer)

# ---- PART TWO ----

answer = 0

for line in lines:
    if validate2(*parse(line)):
        answer += 1

print ("Answer2: ", answer)


