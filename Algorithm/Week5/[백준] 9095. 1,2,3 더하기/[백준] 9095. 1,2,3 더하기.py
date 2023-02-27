# 1. 테스트 케이스의 개수 T 입력 받기
T = int(input())

# 2. DP로 풀기 위해 함수 생성
#   케이스별로 나열해서 규칙을 구한 결과 다음과 같은 점화식이 나오게 됨
#   n > 3 일 때, f(n) = f(n-1) + f(n-2) + f(n-3)
#   이를 재귀로 구현한 함수가 case_num이다.
def case_num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return case_num(n-1) + case_num(n-2) + case_num(n-3)
  
for i in range(T):
    n = int(input())
    print(case_num(n))
