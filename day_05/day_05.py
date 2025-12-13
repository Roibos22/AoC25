import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(ranges, ids):
    res = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                res += 1
                break
    return res

def part_two(ranges, ids):
    pass

def main():
    ranges_str, ids_str = open(filename).read().strip().split('\n\n')
    ranges = [tuple(map(int, r.split('-'))) for r in ranges_str.splitlines()]
    ids = [int(i) for i in ids_str.splitlines()]
    print(ranges, ids)
    print("Part 1 -> ", part_one(ranges, ids))
    print("Part 2 -> ", part_two(ranges, ids))

main()