import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(n):
    lst = list(map(int,input().split()))
    if sum(lst)/len(lst) >= 60:
        print('pass')
        count += 1
    else:
        print('fail')

print(count)