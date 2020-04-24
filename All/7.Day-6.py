T = int(input())

for i in range(T):
    word   = str(input())
    length = len(word)

    even = word[0]
    odd  = word[1]

    for i in range(length):
        if(i==0 or i==1):
            continue
        elif i%2==0:
            even += word[i]
        else:
            odd += word[i]

    print(even+'  '+odd)
