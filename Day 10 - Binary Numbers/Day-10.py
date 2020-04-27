data = []
n = int(input())

while n > 0:
    value =  n%2
    data.append(value)
    n = n//2

#print(data) # for 13 = 1011

data.reverse() # for 13 = 1101 (actual)

count = 0
max_consecutive_1s = 0

for i in range(len(data)):
    if data[i]==1:
        count = count + 1
        if count > max_consecutive_1s:
            max_consecutive_1s = count
    else:
        count = 0
        
print(max_consecutive_1s)