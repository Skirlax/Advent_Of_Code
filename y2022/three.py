def load_file():
    with open("inputs/input3.txt") as file:
        cont = file.read()
        file.close()

    return cont


def solve():
    content = load_file()
    lines = content.split("\n")
    alphabet_pri_lower = []
    alphabet_pri_upper = []
    for line in lines:
        comp1 = line[0:len(line) // 2]
        comp2 = line[len(line) // 2:]
        shared = list(set([x for x in comp1 if x in comp2]))
        alphabet_pri_lower.extend([(ord(x) - ord('a')) + 1 for x in shared if x.islower()])
        alphabet_pri_upper.extend([(ord(x.lower()) - ord("a")) + 27 for x in shared if x.isupper()])

    alphabet_pri_upper.extend(alphabet_pri_lower)
    x = sum(alphabet_pri_upper)
    print(x)


def solve_part_two():
    content = load_file()
    lines = content.split("\n")
    lines3 = [lines[idx:idx+3] for idx in range(len(lines)) if idx % 3 == 0]
    alphabet_pri_lower = []
    alphabet_pri_upper = []
    for line in lines3:
        shared = list(set([x for x in line[0] if x in line[1] and x in line[2]]))
        alphabet_pri_lower.extend([(ord(x) - ord('a')) + 1 for x in shared if x.islower()])
        alphabet_pri_upper.extend([(ord(x.lower()) - ord("a")) + 27 for x in shared if x.isupper()])

    alphabet_pri_upper.extend(alphabet_pri_lower)
    x = sum(alphabet_pri_upper)
    print(x)


if __name__ == "__main__":
    solve_part_two()
