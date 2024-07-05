#Given a list of names, count the number of names that
#start with a vowel


#function definition to count names

def count_name(name_list):
    
    vowel="aeiouAEIOU"  #string containing all vowels
    
    result=list()
    for i in name_list:
        
        if i[0] in vowel:
            result.append(i)
            
    return result

#code

name_list=list()
n=int(input("Enter the number of names in list: "))

for i in range(0,n,1):
    
    name=str(input(f"Enter name [{i+1}]"))
    name_list.append(name)
    
result_list=count_name(name_list)

print(f"The list of names starting with vowel are \n {result_list}")
            
            
