N = int(input())
s = list(map(int, input().split()))

num = 0
s.sort()

for i in range(N):
    for j in range(i + 1):
        num += s[j]
        
print(num)
