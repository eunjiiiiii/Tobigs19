N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]
res = [0, 0]

def traversal(x, y, N):
    color = PAPER[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != PAPER[row][col]:    
                # 다른 곳이 있다면 다시 네 구역으로 나눠서 재귀 수행 
                traversal(x, y, N // 2)
                traversal(x, y + N // 2, N // 2)
                traversal(x + N // 2, y, N // 2)
                traversal(x + N // 2, y + N // 2, N // 2)
                return 0    # 모두 같은 색이 있으면 0 반환
            
    if color == 0: # 범위 내에서 색깔이 모두 같다면
        res[0] += 1
    else:    
        res[1] += 1

traversal(0, 0, N) # 0,0부터 시작
for r in res:
    print(r)
