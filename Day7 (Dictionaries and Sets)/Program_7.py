#Given two sets, find the union, intersection, and
#difference between them


#code

set1=set({'a','j','k','L','o','p'})
set2=set({'p','t','w','k','r','e','m'})

print(f"Two sets are:\n{set1}\n{set2}")

print(f"unioun of both sets is\n {set1.union(set2)}")
print(f"Intersection of both sets is\n {set1.intersection(set2)}")
print(f"Difference of both sets is\n {set1.difference(set2)}") 