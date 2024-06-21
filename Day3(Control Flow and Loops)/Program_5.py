#Given a list of names, print all names starting with the
#letter 'A'


#function to give list of Names starting with letter 'A'

def nameA_list(s_list):
    
    a_list=list()
    
    for i in s_list:
        
        name=i
        if(name[0]=='A'):
            
            a_list.append(name)
            
    return a_list

#code to take names and print required output
name_list=list()

n=int(input("Enter the number of names in List: "))


for i in range(0,n,1):
    
    name=str(input(f"Enter the name [{i+1}]: "))
    
    name_list.append(name)
    
    
a_list=nameA_list(name_list)
#if list is empty or not 
if(a_list):
    print(f"The names starting with letter 'A' are: \n {a_list}")
    
else:
    print("There are no any names starting with letter 'A'")