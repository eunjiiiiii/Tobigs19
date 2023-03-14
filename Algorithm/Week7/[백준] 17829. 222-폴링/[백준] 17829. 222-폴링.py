N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def pooling(length, x, y):
    half = length // 2
    if length == 2:
        res = [matrix[x][y], matrix[x+1][y], matrix[x][y+1], matrix[x+1][y+1]]
        res.sort()
        return res[-2]
    left_top = pooling(half, x, y)
    right_top = pooling(half, x + half, y)
    left_bottom = pooling(half, x, y + half)
    right_bottom = pooling(half, x + half, y + half)
    res = [left_top, right_top, left_bottom, right_bottom]
    res.sort()
    return res[-2]

print(pooling(N,0,0))
