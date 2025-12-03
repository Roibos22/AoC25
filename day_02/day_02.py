import sys


test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"


def part_one(data):
    res = 0
    for ip_range in data:
        l, r = map(int, ip_range.split('-'))
        for x in range(l, r+1):
            digits = len(str(x))
            if digits % 2 != 0:
                continue
            if str(x)[:(int(digits/2))] == str(x)[(int(digits/2)):]:
                res += x
    return(res)


def part_two(data):
    res = 0
    for ip_range in data:
        start, end = map(int, ip_range.split('-'))
        for x in range(start, end+1):
            digits = len(str(x))
            for size in range(1, int(digits/2+1)):
                chunks = [str(x)[i:i+size] for i in range(0, len(str(x)), size)]
                if all(c == chunks[0] for c in chunks):
                    res += x
                    break
    return(res)


def main():
    data = open(filename).read().split(',')
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))


main()