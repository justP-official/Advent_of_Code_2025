def rotate_left(pos, value):
    result = pos - value

    while result < 0:
        result += 100
    
    return result

def rotate_right(pos, value):
    result = pos + value

    
    if result >= 100:
        result %= 100

    return result


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
