def isRectangular(mat: list[list]) -> bool:
    if not mat: return True
    row_ln = len(mat[0])
    for row in mat:
        if len(row) != row_ln: return False
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")
    if not mat or not mat[0]: return []

    rows = len(mat)
    cols = len(mat[0])
    t_mat = [[None for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            t_mat[j][i] = mat[i][j]
    return t_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")

    res = []
    for row in mat:
        res.append(sum(row))
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")

    rows = len(mat)
    cols = len(mat[0])
    res = [0] * cols

    for i in range(rows):
        for j in range(cols):
            res[j] += mat[i][j]
    return res