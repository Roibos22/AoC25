import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"


def do_calc(line, op):
    res = 0
    if op == '+':
        res += sum(line)
    elif op == '*':
        product = 1
        for num in line:
            product *= num
        res += product
    return res


def part_one(data):
    res = 0
    data = list(line.split() for line in data)
    data = list(zip(*data))
    for line in data:
        op = line[-1]
        line = list(map(int, line[:-1]))
        res += do_calc(line, op)
    return res


def part_two(data):
    res = 0
    ops = data[-1].split()
    data = list(line for line in data[:-1])
    data = list(zip(*data))
    data = list(''.join(line).strip() for line in data)

    op_i = 0
    curr = []
    for i, num in enumerate(data):
        if num != '':
            curr.append(num)
        if num == '' or i == len(data) - 1:
            res += do_calc(list(map(int, curr)), ops[op_i])
            op_i += 1
            curr = []
    return res

def main():
    data = open(filename).read().splitlines()
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()