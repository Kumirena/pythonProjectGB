#Напишите функцию для транспонирования матрицы transposed_matrix,
#принимает в аргументы matrix, и возвращает транспонированную матрицу.


matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
#transposed_matrix = transpose(matrix)
def transpose_matrix(matrix, n, m):
    transposed_matrix = [[0] * n for i in range(m)]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            transposed_matrix[j][i] = val
    return transposed_matrix


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    for row in transpose_matrix(matrix, n, m):
        print(*row)


if __name__ == '__main__':
    main()