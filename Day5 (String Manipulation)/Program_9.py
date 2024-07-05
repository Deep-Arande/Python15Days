# Write a function to remove all duplicate characters from a
#given string


#function definition to remove duplicates

def remove_dup(str1):
    
    unique=str()
    str2=str1.lower()
    
    for i in str2:
        
        if i not in unique:
            
            unique=unique+i
            
    return unique

#code

st=str(input("Enter the string: "))

result=remove_dup(st)

print(f"String after removing duplicates: {result}")