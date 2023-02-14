import itertools
heights = []
for _ in range(9):
    heights.append(int(input()))

for comb in itertools.combinations(heights, 7):  # heights에서 7명의 조합을 for문을 통해 확인
    if sum(comb) == 100:  # 7명의 키의 합이 100이면
        for res in sorted(comb):  # 오름차순 정렬하여 출력
            print(res)
        break