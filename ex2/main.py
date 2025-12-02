def check_id(an_id):
    if len(an_id) % 2 != 0:
        return False
    
    mid = len(an_id) // 2

    left_part, right_part = an_id[:mid], an_id[mid:]

    return left_part == right_part

with open("input2.txt", "r") as file:
    ranges = file.readline().split(",")

total = 0

for r in ranges:
    left_bound, right_bound = map(int, r.split("-"))

    for an_id in range(left_bound, right_bound+1):
        if check_id(str(an_id)):
            total += an_id

print(total)