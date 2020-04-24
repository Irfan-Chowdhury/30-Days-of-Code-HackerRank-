n = int(input())
arr = list(map(int, input().rstrip().split()))

arr.reverse()

reverse_arr = ' '.join([str(v) for v in arr])

print(reverse_arr)
