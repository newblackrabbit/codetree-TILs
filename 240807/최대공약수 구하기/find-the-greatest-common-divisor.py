n,m = map(int,input().split())

for i in range(min(n,m)):
    k = min(n,m) - i
    if n % k  == 0 and m % k == 0:
        print(k)
        break