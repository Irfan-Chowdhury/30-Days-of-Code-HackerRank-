n = int(input())
arr = list(map(int, input().rstrip().split()))

arr.reverse()

#print(" ".join(map(str, arr[::-1])))  #you can use this line

reverse_arr = ' '.join([str(v) for v in arr])

print(reverse_arr)





'''
my_list = []
T = int(input())

for i in range(T):
    number = int(input())
    my_list.append(number)

#my_list.reverse()
print(my_list[::-1])
'''
'''
    
length = len(my_list)
reverse = my_list[length-1]
#print(length)
#print(reverse)

for i in range(length-1,0,-1):
    data = int(reverse[i])
    reverse.append(data)

print(reverse)
'''


'''
for i in range(10-1, -1, -1):
     print(i)
'''
