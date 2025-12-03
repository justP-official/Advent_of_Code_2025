def find_max_joltage(seq):
    nums = tuple(map(int, list(seq)))

    max_joltage = 0

    for j in range(len(nums)):
        for i in range(j):
            num = nums[i] * 10 + nums[j]

            if num > max_joltage:
                max_joltage = num
    
    return max_joltage


total = 0

with open("input3.txt", "r") as file:
    for row in file.readlines():

        total += find_max_joltage(row.strip())

print(total)