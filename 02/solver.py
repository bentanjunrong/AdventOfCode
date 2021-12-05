with open("input.txt") as f:
    lines = f.readlines()

hor = 0
depth = 0
for line in lines:
    instruction, value = line.split()
    if instruction == "forward":
        hor += int(value)
    elif instruction == "down":
        depth += int(value)
    elif instruction == "up":
        depth -= int(value)

print(hor * depth)

hor = 0
depth = 0
aim = 0
for line in lines:
    instruction, value = line.split()
    if instruction == "forward":
        hor += int(value)
        depth = depth + (aim * int(value))
    elif instruction == "down":
        aim += int(value)
    elif instruction == "up":
        aim -= int(value)

print(hor * depth)
