# 1. 포도주 잔의 개수 입력받기
n = int(input())

# 2. 포도주 양 입력 받기
wines = [int(input()) for i in range(n)]

# 3. dp 리스트 생성
dp = [0] * n
dp[0] = wines[0]

# 4. 마실 수 있는 최대 포도주의 양 dp에 저장하기
# 점화식 구현
if n > 1:
    dp[1] = wines[1] + wines[0]

if n > 2:
    dp[2] = max(wines[2] + wines[1], wines[2] + wines[0], dp[1])

for i in range(3, n):
    # 현재 포도주를 마실지 말지를 결정하는 코드
    # 1) 현재 포도주는 마시지 않는 경우
    # 2) 현재 포도주와 이전 포도주를 마시고 두번째 전 포도주는 마시지 않는 경우
    # 3) 현재 포도주와 두번째 전 포도주를 마시고 이전 포도주는 마시지 않는 경우
    # 1), 2), 3) 중 가장 양이 큰 경우를 i번째 dp에 저장한다.
    dp[i] = max(dp[i-1], dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i])

# 최종 최대값 출력
print(dp.pop())