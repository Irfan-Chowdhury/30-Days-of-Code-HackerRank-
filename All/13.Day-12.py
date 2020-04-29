#============= Way - 1 ===============

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        data = self.scores

        sumData = sum(data)
        dataLength = len(data)
        avg = sumData // dataLength

        letter = ['O', 'E', 'A', 'P', 'D', 'T']

        if avg >= 90 and avg <= 100:
            return letter[0]
        elif avg >= 80 and avg < 90:
            return letter[1]
        elif avg >= 70 and avg < 80:
            return letter[2]
        elif avg >= 55 and avg < 70:
            return letter[3]
        elif avg >= 40 and avg < 55:
            return letter[4]
        else:
            return letter[5]


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


#============= Way - 2 ===============
'''

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(firstName,lastName,idNumber)
        self.scores = scores

    def calculate(self):
        data = self.scores

        sumData = sum(data)
        dataLength = len(data)
        avg = sumData // dataLength

        if avg >= 90 and avg <= 100:
            return 'O'
        elif avg >= 80 and avg < 90:
            return 'E'
        elif avg >= 70 and avg < 80:
            return 'A'
        elif avg >= 55 and avg < 70:
            return 'P'
        elif avg >= 40 and avg < 55:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

'''