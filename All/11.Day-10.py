# ======= Decimal To Binary - Using List ======
'''
data = []
print("Enter the number to convert:")
n = int(input())

while n>0:
    value =  n%2
    data.append(value)
    n=n//2
    
data.reverse()

listToStr =  ''.join([str(elem) for elem in data])
print("Binary of the given number = "+listToStr)
'''


# =======#Day-10 Decimal To Binary - Using in-built function
'''
def decimalToBinary(n):
    return bin(n).replace("0b", "")

n = int(input())
print(decimalToBinary(n))
'''


# ======= Decimal To Binary - Using Recursion ======
'''
def DecimalToBinary(num): 
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
  
# decimal value 
value = int(input())
      
# Calling function 
DecimalToBinary(value) 
'''


# ========#Day-10 Maximum Consecutive 1’s in Binary Representation ======== 

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

