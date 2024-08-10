def year(n):
    if n % 4 == 0:
        return True
    return False

y = int(input())

if year(y) == True:
    print('true')
else:
    print('false')

year(y)