import sys
input = sys.stdin.readline

n = int(input())


num = list(map(int,input().split()))

ans = []

for i in num:
    if i % 2 == 0:
        ans.append(i)

ans = ans[::-1]

for i in ans:
    print(i,end=' ')