from Utility.Tools import *

class LinearAlgebra:
    _2x2ID = [[1, 0], [0, 1]]

    @staticmethod
    def MxS(matrix, scalar):
        return LinearAlgebra.Map(matrix, lambda x: x * scalar)

    @staticmethod
    def MxM(a, b):
        # Ensure matrices can be multiplied
        if len(a[0]) != len(b):
            return LinearAlgebra._2x2ID

        n = len(a)
        p = len(b[0])
        m = len(a[0])

        result = [[0] * p for _ in range(n)]

        for i in range(n):
            for j in range(p):
                sum = 0
                for k in range(m):
                    sum += a[i][k] * b[k][j]
                result[i][j] = sum

        return result

    @staticmethod
    def MxMod(a, b, mod):
        # Ensure matrices can be multiplied
        if len(a[0]) != len(b):
            return LinearAlgebra._2x2ID

        n = len(a)
        p = len(b[0])
        m = len(a[0])

        result = [[0] * p for _ in range(n)]

        for i in range(n):
            for j in range(p):
                sum = 0
                for k in range(m):
                    sum += a[i][k] * b[k][j]
                result[i][j] = sum % mod

        return result

    @staticmethod
    def Map(matrix, app):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = app(matrix[i][j])
        return matrix

    @staticmethod
    def ToInt(matrix):
        return [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

    @staticmethod
    def _2x2Det(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    @staticmethod
    def _2x2Adj(matrix):
        return [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

    @staticmethod
    def _2x2Inverse(matrix):
        inverse_det = 1.0 / LinearAlgebra._2x2Det(matrix)
        adjugate = LinearAlgebra._2x2Adj(matrix)
        return LinearAlgebra.MxS(adjugate, inverse_det)

    @staticmethod
    def _2x2InverseMod(matrix, mod):
        inverse_det = ModularInverse(int(LinearAlgebra._2x2Det(matrix)), mod)
        adjugate = LinearAlgebra._2x2Adj(matrix)
        inverse = LinearAlgebra.MxS(adjugate, inverse_det)
        return LinearAlgebra.Map(inverse, lambda x: x % mod)

    @staticmethod
    def DisplayMatrix(matrix):
        for row in matrix:
            print("|", " ".join(map(str, row)), "|")

    @staticmethod
    def GetColumn(matrix, index):
        return [matrix[i][index] for i in range(len(matrix))]

    @staticmethod
    def SetColumn(matrix, column, index):
        for i in range(len(column)):
            matrix[i][index] = column[i]
        return matrix

    @staticmethod
    def MatrixToString(matrix):
        output = "{"
        for row in matrix:
            output += str(row).replace("[", "{").replace("]", "}")
            output += ", "
        output = output[:-2]  # Remove the last comma and space
        output += "}"
        return output

    @staticmethod
    def MatrixToStringInt(matrix):
        output = "{"
        intMatrix = LinearAlgebra.ToInt(matrix)
        for row in intMatrix:
            output += str(row).replace("[", "{").replace("]", "}")
            output += ", "
        output = output[:-2]  # Remove the last comma and space
        output += "}"
        return output