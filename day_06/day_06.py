import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(data):
    res = 0
    data = zip(*data)
    for line in data:
        operator = line[-1]
        line = list(map(int, line[:-1]))
        if operator == '+':
            res += sum(line)
        elif operator == '*':
            product = 1
            for num in line:
                product *= num
            res += product
    return res

def part_two(data):
    pass

def main():
    data = [line.split() for line in open(filename).read().splitlines()]
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()