def rotate_left(pos, value):
    tmp = pos - value

    while tmp < 0:
        tmp += 100
    
    return tmp

def rotate_right(pos, value):
    tmp = pos + value

    
    while tmp >= 100:
        tmp -= 100

    return tmp


OPERATORS = {
    "L": rotate_left,
    "R": rotate_right
}

pos = 50

password = 0


with open("input1.txt", "r") as file:
    for row in file.readlines():
        direction, value = row[0], int(row[1:])

        pos = OPERATORS[direction](pos, value)

        if pos == 0:
            password += 1

print("password:", password)
