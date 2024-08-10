def year(y):
    if y % 4 == 0:
        return True
    if y % 100 == 0 and y % 400 != 0:
        return False
    return False

y = int(input())

if year(y) == True:
    print('true')
else:
    print('false')

year(y)