import sys
input = sys.stdin.readline
lst = []
num = list(map(int,input().split()))

lst.append(num[2])
lst.append(num[4])
lst.append(num[9])

print(sum(lst))