import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(lines):
    res = 0
    pos = 50

    for line in lines:
        if line[0] == 'L':
            pos -= int(line[1:])
        elif line[0] == 'R':
            pos += int(line[1:])
        pos = pos % 100
        res += pos == 0

    return(res)

def part_two(lines):
    res = 0
    pos = 50

    for line in lines:
        dir = 0
        if line[0] == 'L':
            dir = -1
        elif line[0] == 'R':
            dir = 1
        for _ in range(int(line[1:])):
            pos = (pos + dir) % 100
            if pos == 0:
                res += 1

    return(res)

def main():
    data = open(filename).read().splitlines()
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()