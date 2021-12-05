with open('input.txt') as f:
    lines = f.readlines()

counter = 0
for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        counter += 1

print(counter)

with open('input.txt') as f:
    lines = f.readlines()

counter = 0
window = int(lines[0]) + int(lines[1]) + int(lines[2])
for i in range(3, len(lines)):
    prev_window = window
    window = window - int(lines[i-3]) + int(lines[i])
    if window > prev_window:
        counter += 1

print(counter)
