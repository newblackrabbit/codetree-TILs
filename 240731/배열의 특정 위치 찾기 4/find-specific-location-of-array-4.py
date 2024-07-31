lst = list(map(int,input().split()))

for i in lst:
    if i == 0:
        lst = lst[:lst.index(i)]

lst_2 = []

for i in lst:
    if i % 2 == 0:
        lst_2.append(i)

print(len(lst_2),sum(lst_2))