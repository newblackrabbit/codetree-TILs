num = list(map(int,input().split()))
odd = []
even = []

for i in range(len(num)):
    if i % 2 == 0:
        even.append(num[i])
    else:
        odd.append(num[i])

if sum(even) >= sum(odd):
    print(sum(even)-sum(odd))
else:
    print(sum(odd)-sum(even))