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


def part_two(ranges):
    ranges.sort()
    res, max_num = 0, 0
    for start, end in ranges:
        if start > max_num:
            res += end - start + 1
        elif end > max_num:
            res += end - max_num
        max_num = max(max_num, end)
    return res


def main():
    ranges_str, ids_str = open(filename).read().strip().split('\n\n')
    ranges = [tuple(map(int, r.split('-'))) for r in ranges_str.splitlines()]
    ids = [int(i) for i in ids_str.splitlines()]
    print("Part 1 -> ", part_one(ranges, ids))
    print("Part 2 -> ", part_two(ranges))

main()