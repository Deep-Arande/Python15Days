#Calculate the area of a triangle given its base and height
#using a function


#function definition

def area(height,base):
    
    return height*base


height=int(input("Enter the height: "))
base=int(input("Enter the base: "))

print(f"Area of triangle is: {area(height,base)}")