#  Given a CSV file with product details (name, price, 
# quantity), create a Product class to manage the data



class Product:
    name=str()
    price=int()
    quantity=int()
    
    def __init__(self,name,price,quantity) -> None:
        
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def __str__(self) -> str:
        
        return f"name={self.name}\nprice={self.price}\nQuantity={self.quantity}"
    
    def change_data(self):
        print("Which data you want to change:\n")
        print(f"Name=1\nPrice=2\nQuantity=3\n")
        choice=int(input("Enter: "))
        
        if choice==1:
            name=str(input("Enter required change: "))
            self.name=name
        elif choice==2:
            price=int(input("Enter required change: "))
            self.price=price
        elif choice==3:
            quantity=int(input("Enter required change: "))
            self.quantity=quantity
        else:
            print("Incorrect option choose.")
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        