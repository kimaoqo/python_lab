def transpose(mat: list[list[float | int]]) -> list[list]:
    try:
        size_mat = [len(mat), len(mat[0])]
    except IndexError:
        return []
    else:
        if max(mat, key=len) is not min(mat, key=len):
            return ValueError
        t_mat = [[0 for _ in range(size_mat[0])] for _ in range(size_mat[1])]
        for x in range(size_mat[0]):
            for y in range(size_mat[1]):
                t_mat[y][x] = mat[x][y]
        return t_mat


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if max(mat, key=len) is not min(mat, key=len):
        return ValueError
    return [sum(x) for x in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if max(mat, key=len) is not min(mat, key=len):
        return ValueError
    return [sum(x) for x in transpose(mat)]