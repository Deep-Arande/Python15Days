#Create a class to represent a Student with attributes like 
#name, age, and grades


class student:
    grades=99
    def __init__(self,name,age,grades): #constructor in python 
        
        self.name=name  #self is used access variable in this instance
        self.age=age
        self.grades=grades

    def __str__(self): #function to return after print on object
        
        return f"{self.name}\n{self.age}\n{self.grades}"


st1=student("Deep",20,98)

print(st1)

#output -> Deep
#           20
#           98  (overrides grade=99 to grade=98)