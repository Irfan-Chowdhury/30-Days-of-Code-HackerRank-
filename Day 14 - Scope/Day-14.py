class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        data = list(map(int, self.__elements))
        length = len(data)

        max_value = []
        n=0

        while(n < length):
            for i in range(n+1,length,1):
                result = abs(data[n] - data[i])
                max_value.append(result)      
            n=n+1

        self.maximumDifference = max(max_value)
     
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)