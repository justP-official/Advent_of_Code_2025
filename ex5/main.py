ranges = []
ids = []

current = ranges

total = 0

with open("input5.txt", "r") as file:
    for row in file.readlines():
        if row == "\n":
            current = ids

        if row != "\n":
            current.append(row.strip())


ranges = [tuple(map(int, r.split("-"))) for r in ranges]

ids = [int(x) for x in ids]


for item_id in ids:
    
    for r in ranges:
        left, right = r

        if left <= item_id <= right:
            total += 1
            break

print(total)