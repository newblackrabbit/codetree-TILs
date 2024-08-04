arr = [0,0,0,0,0,0,0,0,0,0,0,0]
arr[0],arr[1] = map(int,input().split())
for i in range(0,10):
    arr[i+2] = arr[i] + arr[i+1]
    arr[i] = arr[i] % 10
for i in range(10):
    print(arr[i],end=' ')