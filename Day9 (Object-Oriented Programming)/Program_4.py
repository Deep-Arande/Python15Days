#Write a Python program that uses a Rectangle class to 
#calculate the area and perimeter of a rectangle


class area_peri:

    __lenght=int()
    __breadth=int()
    def __init__(self,l,b):
        self.__lenght=l
        self.__breadth=b
    
    def area(self):
        
        return int(self.__lenght*self.__breadth)

    def perimeter(self):
        
        return int(2*(self.__lenght+self.__breadth))

    def __str__(self):
        return f"lenght={self.__lenght},breadth={self.__breadth}"

r1=area_peri(23,56)

print(r1.area())
print(r1.perimeter())
print(r1)
        
