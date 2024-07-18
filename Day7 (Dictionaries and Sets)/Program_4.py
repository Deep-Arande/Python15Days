#Create a program that checks if two sets have any
#elements in common 



#code

set1=set({"A","D","E","R","T"})
set2=set({"A","B","k","Z"})

if set1.intersection(set2):
    
    print(f"The two sets have some elements common:\n{set1.intersection(set2)}")
else:
    print("Sets don't have common elements:")