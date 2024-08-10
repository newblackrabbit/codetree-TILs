def year(y):
    if y % 4 == 0:
        return True
    return False

y = int(input())

if year(y) == True:
    print('true')
else:
    print('false')

year(y)