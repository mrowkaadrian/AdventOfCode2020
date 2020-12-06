import re


def read_passports(_filename):
    file_content = open(_filename, 'r').readlines()
    passports = []
    temp_passport = {}

    for line in file_content:
        if line == "\n":
            passports.append(dict(temp_passport))   # append a copy instead of reference
            temp_passport.clear()
        else:
            data = line.strip()
            for field in data.split(" "):
                item = field.split(":")
                temp_passport.update({item[0]: item[1]})

    return passports


def is_valid(_passport):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in keys:
        if key not in _passport:
            return False
    return True


def validate_byr(byr):
    return byr.isdigit and len(byr) == 4 and 1920 <= int(byr) <= 2002


def validate_iyr(iyr):
    return iyr.isdigit and len(iyr) == 4 and 2010 <= int(iyr) <= 2020


def validate_eyr(eyr):
    return eyr.isdigit and len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def validate_hgt(hgt):
    return "cm" in hgt and 150 <= int(hgt[:-2]) <= 193 or "in" in hgt and 50 <= int(hgt[:-2]) <= 76


def validate_hcl(hcl):
    return len(hcl) == 7 and re.search("^#[a-fA-F0-9]{6}", hcl)


def validate_ecl(ecl):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for color in colors:
        if color == ecl:
            return True
    return False


def validate_pid(pid):
    return pid.isdigit and len(pid) == 9


def validate_field_values(_passport):
    return validate_byr(_passport.get('byr')) and validate_iyr(_passport.get('iyr')) and validate_eyr(_passport.get('eyr')) \
           and validate_hgt(_passport.get('hgt')) and validate_hcl(_passport.get('hcl')) and validate_ecl(_passport.get('ecl')) \
           and validate_pid(_passport.get('pid'))


# ---- PART ONE ----

all_passports = read_passports("input.txt")
result = 0

for passport in all_passports:
    if is_valid(passport):
        result += 1

print result

# ---- PART TWO ----

result = 0

for passport in all_passports:
    if is_valid(passport):
        if validate_field_values(passport):
            result += 1

print result
