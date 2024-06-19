#Calculate the area and circumference of a circle given its radius

def circumference_area(radius):
    
    area=float(3.14*(radius**2))
    cirumference=float(2*3.14*radius)
    
    n_list=list()
    
    n_list.append(area)
    n_list.append(cirumference)
    
    return n_list



r=int(input("Enter the radius of circle: "))

component=circumference_area(r)

print(f"The area of circle is: {component[0]} and circumference is: {component[1]}")