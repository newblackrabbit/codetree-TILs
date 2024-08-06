n = int(input())

def num(n):
    count = 1
    for i in range(n):
        for i in range(n):
            print(count,end=' ')
            count += 1
            if count == 10:
                count = 1
        print()

num(n)