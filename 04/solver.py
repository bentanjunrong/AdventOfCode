with open("input.txt") as f:
    lines = f.readlines()


def is_bingo(matrix):
    for i in range(len(matrix)):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == matrix[i][3] == True:
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == matrix[3][i] == True:
            return True
    return False


order = [int(ele) for ele in lines[0].split(",")]
big_matrix = []
mini_matrix = []
i = 0
for line in lines[1:]:
    val = [int(ele) for ele in line.split()]
    if len(val):
        mini_matrix.append(val)
        i += 1
        if i == 5:
            big_matrix.append(mini_matrix)
            mini_matrix = []
            i = 0
