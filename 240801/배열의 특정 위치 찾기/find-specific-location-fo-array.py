num = list(map(int,input().split()))
num2 = 0
num3 = 0
count = 0

for i in range(10):
    if (i+1) % 2 == 0:
        num2 += num[i]
    if (i+1) % 3 == 0:
        num3 += num[i]
        count += 1


avg3 = num3 / count
print(num2,round(avg3,1))