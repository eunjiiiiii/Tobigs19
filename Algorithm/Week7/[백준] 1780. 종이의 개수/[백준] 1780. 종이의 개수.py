import sys

N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

# 결과 저장할 딕셔너리 생성, 종류를 key로 종류의 개수를 value로 한다.
result = {-1:0, 0:0,1:0}

# 종이의 종류(-1, 0, 1)와 다르면 분할(분할정복)
def divided(x,y,n):
    curr = paper[x][y] 

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != curr:
                # 현재 종이와 다른 종류라면 종이를 1/3로 분할
                next_paper = n // 3
                
                # 9개로 나누기
                divided(x, y, next_paper) # 1번째 block (0,0)
                divided(x, y + next_paper, next_paper) # 2번째 block (0,1)
                divided(x, y + (next_paper*2), next_paper) # 3번째 block (0,2)
                divided(x + next_paper, y, next_paper) # 4번째 block (1,0)
                divided(x + next_paper, y + next_paper, next_paper) # 5번째 block (1,1)
                divided(x + next_paper, y + (next_paper*2), next_paper) # 6번째 block (1,2)
                divided(x + (next_paper*2), y, next_paper) # 7번째 block (1,0)
                divided(x + (next_paper*2), y + next_paper, next_paper) # 8번째 block (1,1)
                divided(x + (next_paper*2), y + (next_paper*2), next_paper) # 9번째 block (1,2)
                return 

    # 종이 종류별로 count 
    result[curr] +=1 
    return 


divided(0,0,N)

for res in result.values():
    print(res)
