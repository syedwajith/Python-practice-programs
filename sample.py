class Student:
    def getStudentInfo(self):
        self.rollno = input("Enter Roll No : ")
        self.name = input("Enter Name : ")

    def displayStudentInfo(self):
        print("Roll Number : ", self.rollno)
        print("Name        : ",self.name)

class BE(Student):
    def getBE(self):
        self.getStudentInfo()
        self.p = int(input("Enter Physics Marks : "))
        self.c = int(input("Enter Chemistry Marks : "))
        self.m = int(input("Enter Maths Marks : "))
    
    def displayBE(self):
        self.displayStudentInfo()
        print("Marks in Subjects!!!")
        print("Physics : ",self.p)
        print("Chemistry : ",self.c)
        print("Maths : ",self.m)

    def calTotalMark(self):
        return(self.p + self.c + self.m)

class Result(BE):
    def getResult(self):
        self.getBE()
        self.total = self.calTotalMark()

    def putResult(self):
        self.displayBE()
        print("Total Marks out of 300 : ",self.total)

obj = Result()
obj.getResult()
obj.putResult()



