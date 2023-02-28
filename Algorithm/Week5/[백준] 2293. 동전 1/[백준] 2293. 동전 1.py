# 1. n, k 입력받기
n, k = map(int, input().split())

# 2. coin 종류 입력 받기
coins = []
for i in range(n):
    coins.append(int(input()))

# 3. dp 리스트 만들기
dp = [0] * (k+1)
dp[0] = 1

# 4. for문 통해서 경우의 수 누적 합 구하기
for c in coins: # coin 종류를 돌면서
    for j in range(c, k+1): # 앞에 탐색한 경우는 제외하고, 주어진 합에서 동전을 뺸 수가 양수이면
        # 즉, coin을 더 이용해서 합을 만들어야 할 경우이면
        p_case = dp[j - c]
        dp[j] += p_case

print(dp[k])    # 구하고자 하는 합의 경우의 수 출력하기