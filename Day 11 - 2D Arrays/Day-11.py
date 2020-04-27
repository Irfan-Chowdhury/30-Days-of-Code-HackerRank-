Arr=[]
for i in range(6):
    data = list(map(int,input().split()))
    Arr.append(data)
    
sum = []
for r in range(4):
    for c in range(4):
        sum.append(Arr[r][c]+Arr[r][c+1]+Arr[r][c+2] + Arr[r+1][c+1] + Arr[r+2][c]+Arr[r+2][c+1]+Arr[r+2][c+2])

print(max(sum))