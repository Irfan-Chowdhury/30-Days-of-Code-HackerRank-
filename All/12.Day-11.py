#===============  2D Array =============== 
'''
Day 1 - 11 12 5 2 
Day 2 - 15 6 10 
Day 3 - 10 8 12 5 
Day 4 - 12 15 8 6 
'''

''' T=[[11,12,5,2],[15,6,10],[10,8,12,5],[12,15,8,6]]   '''

#1.===============  Accessing Values in a Two Dimensional Array =============== 
'''
print(T)
print(T[0])
print(T[1][2])

#For Loop
for i in T:
    for j in i:
        print(j,end=" ")
    print()
'''
    
#2.===============  Inserting Values in Two Dimensional Array =============== 
'''
T.insert(2,[0,5,11,13,6])
for i in T:
    for j in i:
        print(j,end=" ")
    print()
'''

#3.===============  Updating Values in Two Dimensional Array =============== 
'''
T[2]=[11,9]
T[0][3]= 7
for i in T:
    for j in i:
        print(j,end=" ")
    print()
'''

#4.=============== Deleting the Values in Two Dimensional Array =============== 
'''
del T[3]
for i in T:
    for j in i:
        print(j,end=" ")
    print()
'''

#5.=============== Insert value in 2-D Array by For Loop ============
'''
Arr=[]

print("How Many Row: ")
rows = int(input())

print("How Many Column: ")
cols = int(input())

print("Insert The Value in array :")
'''

#1 <-----take input 1 by 1 line ------>
'''
for i in range(rows):
    col = []
    for j in range(cols):
        value = int(input())
        col.append(value)
    Arr.append(col)
'''


#2 <-----take input by separate space in each line------>
'''
for i in range(rows):
    data = list(map(int,input().split()))
    Arr.append(data)
'''

'''
print("\nYour Output (way-1) :")
print(Arr)
print("\nYour Output (way-2) :")

for row in Arr:
    for col in row:
        print(col,end=" ")
    print()
'''
#============================= Day 11: 2D Array ====================
Arr=[]
for i in range(6):
    data = list(map(int,input().split()))
    Arr.append(data)
    
sum = []
for r in range(4):
    for c in range(4):
        sum.append(Arr[r][c]+Arr[r][c+1]+Arr[r][c+2] + Arr[r+1][c+1] + Arr[r+2][c]+Arr[r+2][c+1]+Arr[r+2][c+2])

print(max(sum))


