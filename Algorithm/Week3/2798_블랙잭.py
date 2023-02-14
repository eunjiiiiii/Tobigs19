import itertools

# 입력 받기
n,m = map(int, input().split())
cards = list(map(int, input().split()))

# 3장 조합 구하기
combs = itertools.combinations(cards, 3)

# 3장 조합 합 최대값 구하기
comb_sum = []
for comb in combs:
    if sum(comb) <= m: # m 넘지 않으면
        comb_sum.append(sum(comb))

print(max(comb_sum))