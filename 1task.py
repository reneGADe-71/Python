class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str("\n".join(["\t".join([str(y) for y in i]) for i in self.lst]))

    def __add__(self, other):
        m = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

        for i in range(len(self.lst)):
            for j in range(len(other.lst[i])):
                m[i][j] = self.lst[i][j] + other.lst[i][j]

        return str("\n".join(["\t".join([str(y) for y in i]) for i in m]))


matrix1 = Matrix([[1, 1, 1],
                  [0, 1, 1],
                  [0, 0, 1]])
matrix2 = Matrix([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0]])

print(matrix1.__str__())
print("---------")
print(matrix2.__str__())
print("---------")
print(matrix1.__add__(matrix2))
