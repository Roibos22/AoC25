import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(data):
    beams = [data[0].index('S')]
    res = 0
    for i, _ in enumerate(data[1]):
        if data[0][i] == 'S':
            data[1][i] = '|'
    for y, row in enumerate(data):
        if y == 0:
            continue
        for x, _ in enumerate(row):
            if data[y-1][x] == '|':
                if data[y][x] == '^':
                    res+=1
                    data[y][x-1] = '|'
                    data[y][x+1] = '|'
                else:
                    data[y][x] = '|'
        print(row)
    return res

def part_two(data):
    pass

def main():
    data = list(list(row) for row in open(filename).read().splitlines())
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()


