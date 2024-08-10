def year(n):
    if n % 4 == 0:
        print('true')
    elif n % 100 == 0 and y % 400 != 0:
        print('false')
    else:
        print('false')
    return None

y = int(input())

year(y)