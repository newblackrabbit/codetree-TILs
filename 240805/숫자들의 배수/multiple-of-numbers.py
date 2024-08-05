n = int(input())
lst = []
count = 0

for i in range(1,11):
    lst.append(i*n)

for i in range(len(lst)):
    if lst[i] % 5 == 0:
        count += 1
    if count == 2:
        lst = lst[:i+1]
        break

for i in lst:
    print(i,end=' ')