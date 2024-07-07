#Create a program that finds the common elements
#between two lists and stores them in a new list


#function to store common elements in list 

def common_list(list1,list2):
    #using list comprehension
    c_list=[i for i in list1 if i in list2]

    return c_list
    

#code

list1=[23,45,63,12,83,64,78]
list2=[35,67,63,83,78]

c_list=common_list(list1,list2)

print(f"Common elements in the lists are:\n {c_list}")
        