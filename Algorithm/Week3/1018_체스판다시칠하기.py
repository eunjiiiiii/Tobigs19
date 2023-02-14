n, m = map(int, input().split())
brd = []
cnt = []

for _ in range(n):
    brd.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        b_cnt = 0
        w_cnt = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if brd[a][b] != 'B':
                        b_cnt += 1
                    if brd[a][b] != 'W':
                        w_cnt += 1
                else:
                    if brd[a][b] != 'W':
                        b_cnt += 1
                    if brd[a][b] != 'B':
                        w_cnt += 1

        cnt.append(b_cnt)
        cnt.append(w_cnt)

print(min(cnt))
