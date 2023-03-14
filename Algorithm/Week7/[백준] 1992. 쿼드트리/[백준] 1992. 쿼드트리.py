N = int(input())
IMAGE = [input().strip() for _ in range(N)]
answer = ""


def comp(x, y, N):
    check = IMAGE[x][y]
    global answer    # global 변수로 선언해준 이유는 재귀로 계속 comp를 불러오기 때문이다.
    
    # 이미지를 4등분하여 1또는 0만 가지는 정사각형 범위를 계속 찾기
    for row in range(x, x + N):
        for col in range(y, y + N):
            if check != IMAGE[row][col]:    # 이전과 다른 값(0 또는 1)이면
                answer += '('    # 압축 시작 괄호 열어주고
                # 사분면 탐색하면서 1또는 0만 가지는 정사각형 범위 즉 압축할 범위 찾기
                # 4등분 중 1사분면
                comp(x, y, N // 2)
                # 4등분 중 2사분면
                comp(x, y + N // 2 , N // 2)
                # 4등분 중 3사분면
                comp(x + N // 2, y , N // 2)
                # 4등분 중 4사분면
                comp(x + N // 2, y + N // 2, N // 2)
                answer += ')'    # 압축이 끝났다는 괄호 닫아주기
                return None
    if check == '0':
        answer += '0'
    else:
        answer += '1'
    return None


comp(0, 0, N)
print(answer)

