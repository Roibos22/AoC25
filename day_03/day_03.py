import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def get_highest_num(nums: list[int]) -> tuple[int, int]:
    max_num = nums[0]
    max_i = 0
    for pos, num in enumerate(nums):
        if num > max_num:
            max_num = num
            max_i = pos
    return(max_num, max_i)

def get_total_joltage(size: int, data) -> int:
    total_joltage = 0
    for bank in data:
        max_jolt = ""
        for i in range(size):
            max_num, max_idx = get_highest_num(bank[:(i-(size-1))] if i < size-1 else bank)
            bank = bank[max_idx+1:]
            max_jolt = max_jolt + str(max_num)
        total_joltage += int(max_jolt)
    return(total_joltage)

def main():
    data = open(filename).read().splitlines()
    print("Part 1 -> ", get_total_joltage(2, data))
    print("Part 2 -> ", get_total_joltage(12, data))

main()