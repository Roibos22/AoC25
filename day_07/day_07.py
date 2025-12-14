import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

data = list(list(row) for row in open(filename).read().splitlines())
data[0] = [s.replace('S', '|') for s in data[0]]


def part_one(data):
    res = 0
    for r, row in enumerate(data):
        for c, _ in enumerate(row):
            if data[r-1][c] == '|':
                if data[r][c] == '^':
                    res+=1
                    data[r][c-1] = '|'
                    data[r][c+1] = '|'
                else:
                    data[r][c] = '|'
    return res


def part_two(data):
    cache = {}

    def solve(r, c):
        if r >= len(data):
            return 1
        if (r, c) in cache:
            return cache[(r, c)]
        res = 0
        if data[r][c] == '^':
            res = solve(r+1,c+1) + solve(r+1,c-1)
        elif data[r][c] == '.'  or data[r][c] == '|':
            res = solve(r+1, c)
        cache[(r, c)] = res
        return res
    
    return solve(0, data[0].index('|'))


print("Part 1 -> ", part_one(data.copy()))
print("Part 2 -> ", part_two(data.copy()))
