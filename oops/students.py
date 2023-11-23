class Student:
    def __init__(self,name,age,m1,m2,m3,m4):
        self.name=name
        self.age=age
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.tot=0
        self.avg=0

    def total(self):

        self.tot=self.m1+self.m2+self.m3+self.m4

    def average(self):
        if self.tot:
            self.avg=self.tot/4
        
    def __repr__(self):
        return f"Name of the student is {self.name}\nTotal:{self.tot}\nAverage:{self.avg}"

stud1=Student(name="Indhu",age=27,m1=85,m2=82,m3=95,m4=85)
stud1.total()
stud1.average()
print(stud1)

    
