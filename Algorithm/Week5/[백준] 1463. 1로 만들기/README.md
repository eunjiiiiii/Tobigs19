# 문제 풀이 방향

재귀함수로 구현하기 위해 가장 먼저 아래와 같은 구조를 떠올렸다. 

def calc(cnt, x): <br>
</tab>    if x % 3 == 0:    # 3으로 나눠 떨어지면<br>
</t></t>        return calc(cnt+1, x // 3)<br>
</t>    elif x % 2 == 0:    # 2로 나눠 떨어지면<br>
</t></t>        return calc(cnt+1, x // 2)<br>
</t>    else:    # 그 외엔<br>
</t></t>        return calc(cnt+1, x - 1)<br>
