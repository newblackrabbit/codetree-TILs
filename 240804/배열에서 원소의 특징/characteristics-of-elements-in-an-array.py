n = list(map(int,input().split()))

for i in range(10):
    if n[i] % 3 == 0:
        print(n[i-1])
        break