# 1. 입력 받을 계단의 개수 입력 받기
n = int(input())
scores = []
dp = []

# 2. 계단별 점수 입력받기
for i in range(n):
    scores.append(int(input()))

# 3. 첫번쨰 계단을 밟는 경우에 발생할 수 있는 점수 중 max 값 dp에 저장
dp.append(scores[0])
dp.append(max(scores[0] + scores[1], scores[1]))
dp.append(max(scores[0] + scores[2], scores[1] + scores[2]))

# 4. 세번째 계단부터 최대 점수 계산하는 점화식 for문으로 구현
for i in range(3, n):
    dp.append(max(dp[i-2] + scores[i] , dp[i-3] + scores[i] + scores[i-1]))

# 5. 가장 마지막 경우(즉, 총 점수의 최대값) 출력하기
print(dp.pop())
