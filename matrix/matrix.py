class Matrix:
    # def __init__(self, matrix_string: str) -> None:
    #     self.matrix = [[int(each) for each in row.split()]
    #                    for row in matrix_string.splitlines()]
    def __init__(self, matrix_string):
            self.rows = []
            lines = matrix_string.splitlines()

            for line in lines:
                columns = [int(value) for value in line.split()]

                self.rows.append(columns)
    # Note list[int] supported in python 3.9+
    def row(self, index: int) -> list[int]:
        return self.matrix[index-1]

    def column(self, index: int) -> list[int]:
        # return [row[index-1] for row in self.matrix]
        column = []

        for row in self.rows:
            column.append(row[index - 1])

        return column

A = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")

print(A.matrix)

print(A.row(2)[2])

A.row(2)[2] = 74

print(A.row(2)[2])

print(A.column(2))

A.column(2)[0] = 44

print(A.column(2))

# print(A.column(2)[2])

# A.column(2)[2] = 34

# print(A.column(2)[2])

# A.matrix[2][1] = 99

# print(A.column(2)[2])
