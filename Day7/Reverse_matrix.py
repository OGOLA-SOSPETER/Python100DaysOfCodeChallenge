#reversing a matrix

def reversedMethod(mtrx1):
    size = len(mtrx1)
    reversed_mtrx = [[0 for _ in range(size)] for _ in range(size)]
    for a in range(size):
        for b in range(size):
            reversed_mtrx[a][b] = mtrx1[b][a]

    return reversed_mtrx



if __name__ == "__main__":
    mtx = [[3,5,6],[8,9,10]]
    revmtx = reversedMethod(mtx)
    for row in revmtx:
        print(row)
