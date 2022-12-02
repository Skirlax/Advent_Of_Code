def load_file():
    with open("input.txt") as f:
        ct = f.read()
        f.close()
    return ct


class Part1:
    def __init__(self):
        self.content = load_file()
        print(self.solve())

    def solve(self):
        split = self.content.split("\n\n")
        return max([sum([int(y) for y in x.split("\n")]) for x in split])


class Part2:
    def __init__(self):
        self.content = load_file()
        print(self.solve())

    def solve(self):
        split = self.content.split("\n\n")
        tops = []
        list_ = [sum([int(y) for y in x.split("\n")]) for x in split]
        for _ in range(3):
            max_ = max(list_)
            tops.append(max_)
            list_.remove(max_)
        return sum(tops)


if __name__ == "__main__":
    Part1()
    Part2()
