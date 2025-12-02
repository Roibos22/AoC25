import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(data):
    pass

def part_two(data):
    pass

def main():
    data = open(filename).read().splitlines()
    print("Part 1 -> ", part_one(data))
    print("Part 2 -> ", part_two(data))

main()