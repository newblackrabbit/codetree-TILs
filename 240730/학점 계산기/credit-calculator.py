n = int(input())

score = list(map(float,input().split()))
sum_score = 0

for i in range(n):
    sum_score += score[i]

aver = sum_score/n
print(round(aver,1))

if aver >= 4.0:
    print('Perfect')
elif aver >= 3.0:
    print('Good')
else:
    print('Poor')