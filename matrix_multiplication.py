def matrix_multiplication(matrix1, matrix2):
    result = []
    final_res = []
    for i in range(len(matrix1)):
        for k in range(len(matrix2[0])):
            a = 0
            for j in range(len(matrix2)):
                a += matrix1[i][j] * matrix2[j][k]

            result.append(a)

    print(result)


if __name__ == '__main__':
    matrix1 = []
    matrix2 = []

    for i in range(2):
        row, col = map(int, input().split())

        if i % 2 == 0:
            for i in range(row):
                val = list(map(int, input().split()))
                val = [val[i] for i in range(col)]
                matrix1.insert(i, val)
        else:
            for i in range(row):
                val = list(map(int, input().split()))
                val = [val[i] for i in range(col)]
                matrix2.insert(i, val)

    res = matrix_multiplication(matrix1, matrix2)