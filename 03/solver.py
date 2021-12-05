from copy import deepcopy
from collections import defaultdict
with open("input.txt") as f:
    lines = f.readlines()

gamma_rate = 0
epsilon_rate = 0

input_len = len(lines)
freq_counter = defaultdict(int)
final_list = [0 for _ in range(12)]
for line in lines:
    line_list = list(line)[:-1]
    for i in range(len(line_list)):
        if line_list[i] == '1':
            freq_counter[i] += 1

for key, value in freq_counter.items():
    if value >= (input_len/2):
        final_list[key] = 1

gamma_rate = int("".join([str(ele) for ele in final_list]), 2)
epsilon_rate = gamma_rate ^ 0xfff
print((gamma_rate)*(epsilon_rate))


def get_oxygen():
    lines_cpy = deepcopy(lines)
    for i in range(12):
        count_zero, count_one = 0, 0
        if len(lines_cpy) == 1:
            break
        for line in lines_cpy:
            if line[i] == '0':
                count_zero += 1
            else:
                count_one += 1

        if count_one >= count_zero:
            lines_cpy = list(filter(lambda x: x[i] == '1', lines_cpy))
        else:
            lines_cpy = list(filter(lambda x: x[i] == '0', lines_cpy))
    return lines_cpy[0]


def get_carbon():
    lines_cpy = deepcopy(lines)
    for i in range(12):
        count_zero, count_one = 0, 0
        if len(lines_cpy) == 1:
            break
        for line in lines_cpy:
            if line[i] == '0':
                count_zero += 1
            else:
                count_one += 1

        if count_one >= count_zero:
            lines_cpy = list(filter(lambda x: x[i] == '0', lines_cpy))
        else:
            lines_cpy = list(filter(lambda x: x[i] == '1', lines_cpy))
    return lines_cpy[0]


oxygen = int(get_oxygen(), 2)
carbon = int(get_carbon(), 2)
print(oxygen*carbon)
