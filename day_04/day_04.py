import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def part_one(data):
    res = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != '@':
                continue
            neighbours = []
            for dy, dx in dirs:
                if 0 <= y+dy < len(data) and 0 <= x+dx < len(data[y]):
                    neighbours.append(data[y+dy][x+dx])
            if neighbours.count('@') < 4:
                res += 1
    return(res)

def part_two(data):
    pass

def main():
    data = [list(line.strip()) for line in open(filename)]
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()