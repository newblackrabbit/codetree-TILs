num = list(map(int, input().split()))

while True: 
    for i in num:
        if i >= 250:
            num = num[:num.index(i)]
            break
    else:
        break  

if len(num) == 0:
    print(0, 0)
else:
    print(sum(num), round(sum(num) / len(num), 1))