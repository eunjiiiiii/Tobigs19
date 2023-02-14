word = list(input())
res = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)): # 3개의 단어로 쪼개기 위해 지점 2개 지정
        first = word[:i] # 첫 번째 단어
        second = word[i:j] # 두 번째 단어
        third = word[j:] # 세 번째 단어

        # 각 단어 뒤집기
        first.reverse()
        second.reverse()
        third.reverse()

        # 뒤집은 단어를 합쳐서 리스트에 저장
        res.append("".join(first + second + third))

# 리스트에서 가장 작은 단어 출력하기 위해 min함수 이용(아스키 코드 이용해서 min으로 구할 수 있는 듯?)
print(min(res))