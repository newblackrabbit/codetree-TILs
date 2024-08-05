lst = list(map(int,input().split()))

for i in range(len(lst)):
    if lst[i] == 0:
        lst = lst[:i]
        break

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst[i] = lst[i] // 2
    else:
        lst[i] = lst[i] + 3

for i in lst:
    print(i,end=' ')

if len(lst) == 0:
    print(0)