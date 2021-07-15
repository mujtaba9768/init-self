class student:
    school = 'telusko'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is student class... in abc module")


s1 = student (32,53,45)
s2 = student (37,45,67)

print(s1.avg())
print(student.getschool())
student.info()
