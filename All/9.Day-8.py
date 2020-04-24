#This Is Done way-1
'''
import sys

T = int(sys.stdin.readline().strip()) #as like- input()

phoneBook = dict()

for i in range(T):
    data = sys.stdin.readline().strip().split(" ")
    phoneBook[data[0]]=data[1]

name = sys.stdin.readline().strip() #as like- input()
while name:    
    if name in phoneBook:
        phone = phoneBook.get(name)
        print(name+'='+phone)
    else:
        print('Not found')
    name = sys.stdin.readline().strip()
'''

#This is Done way-2
'''
#The Normal Way
import sys

phoneBook = dict()

T = int(sys.stdin.readline().strip()) #as like- input()

for i in range(T):
    name,phone = input().split(" ")
    phoneBook[name]=phone

name = sys.stdin.readline().strip() #as like- input()
while name:    
    if name in phoneBook:
        phone=phoneBook[name]
        print(name+'='+phone)
    else:
        print('Not found')
    name = sys.stdin.readline().strip()
'''








'''
phoneBook = {}
T = int(input())
for i in range(T):
    name,phone = input().split(" ")
    phoneBook[name]=int(phone)
 
for j in range(len(phoneBook)):
    name = input()
    if name in phoneBook:
        print(name+'='+str(phoneBook[name]))
    else:
        print('Not found')
'''




#phoneBook = {"Same":99912222,"tom":11122222,"harry":12299933}
'''
query = str(input())
print(phoneBook.get(query,'Not Found'))
'''

'''
my_marks = {"Bengali":80,"English":85,"Math":90}
my_marks["Math"] = 95
my_marks["Science"] = 76
'''

#print(my_marks.get("English",'Not Found'))

'''
print("Bengali" in my_marks)
print(52 in my_marks)
print("Exercise" not in my_marks)
'''
#print(my_marks)
