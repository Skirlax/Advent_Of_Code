def part_one(file_path: str):
    with open(file_path, "r") as f:
        content = f.readlines()

    output = map(lambda b: int(''.join(b)),
                 map(lambda x: [[y for y in x if y.isdigit()][0], [i for i in reversed(x) if i.isdigit()][0]], content))
    return sum(output)


def part_two(file_path: str):
    with open(file_path, "r") as f:
        content = f.readlines()
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9}
    for index, x in enumerate(content):
        for y in nums.keys():
            content[index] = content[index].replace(y, f"{y[0]}{str(nums[y])}{y[-1]}")

    output = map(lambda b: int(''.join(b)),
                 map(lambda x: [[y for y in x if y.isdigit()][0], [i for i in reversed(x) if i.isdigit()][0]], content))
    return sum(output)


if __name__ == "__main__":
    print(part_two("day1_input.txt"))
