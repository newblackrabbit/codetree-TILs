lst = list(map(int,input().split()))

for i in lst:
    if i == 0:
        lst = lst[:lst.index(i)]
lst = lst[::-1]


print(sum(lst),round(sum(lst)/len(lst),1))