num = list(map(int,input().split()))

for i in range(len(num)):
    if num[i] == 0:
        print(num[i-1]+num[i-2]+num[i-3])
        break