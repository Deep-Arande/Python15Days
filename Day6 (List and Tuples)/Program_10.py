#Implement a function that takes two lists and returns their
#union (all unique elements from both lists)


#function to find union of tow list

def union_list(list1,list2):
    
    u_list=list()
    
    for i in list1:
        
        if i in list2:
            u_list.append(i)
    
    return u_list

#code

list1=[2,6,1,54,50,257,48,92,10]
list2=[2,3,1,54,6,92,257]

r_list=union_list(list1,list2)

print(f"union of lists are:\n {r_list}")