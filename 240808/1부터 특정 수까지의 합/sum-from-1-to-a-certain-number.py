n = int(input())

def plus(n):
    count = 0
    for i in range(1,n+1):
        count += i
    return count//10

print(plus(n))