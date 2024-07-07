#Write a program that finds the largest and smallest
#elements in a list

#code

n_list=[34,56,21,78,34,90,234]


#algo to find largest and smallest number

largest=n_list[0]
smallest=n_list[0]

for i in n_list:
    
     if largest<i:
         largest=i
         
     if smallest>i:
        smallest=i

print(f"The smallest={smallest} and largest={largest}")