import sys

phoneBook = dict()

T = int(sys.stdin.readline().strip())

for i in range(T):
    name,phone = input().split(" ")
    phoneBook[name]=phone

name = sys.stdin.readline().strip() 
while name:    
    if name in phoneBook:
        phone=phoneBook[name]
        print(name+'='+phone)
    else:
        print('Not found')
    name = sys.stdin.readline().strip()