#Create a class to represent a Car with attributes like 
#make, model, and year


class Car:
    
    brand=str()
    model=str()
    year=int()
    
    def __init__(self,brand,model,year)->int:
        
        self.brand=brand
        self.model=model
        self.year=year
    
    def __str__(self) -> str:
        
        return f"brand={self.brand}\n model={self.model}\n year={self.year}"


car1=Car("Honda","fg",2034)

print(car1.brand)
print(car1)
        