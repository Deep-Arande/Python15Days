#Given a list of names, concatenate them into a single
#string separated by spaces


#function definition to concatenate strings

def str_concatenet(s_list):
    
    str1=str()
    
    for i in s_list:
        str1=str1+i+' '
        
    return str1

#list to take names
st_list=[]

n=int(input("Enter the number of names in list: "))

for i in range(0,n,1):
    
    name=str(input(f"Enter the name [{i+1}]: "))
    st_list.append(name)
    

name_str=str_concatenet(st_list)

print(f"All names in a single string is:\n {name_str}")