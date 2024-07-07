#Given a list of names, remove all duplicate names and
#print the unique names

#function to return list of unique names

def unique_names(name_list):
    
    unique_list=list()
    
    for i in name_list:
        
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

#code

name_list=["Kedar","Kedar","Deep","Samarth","Samarth","shlok","Deep","Kedar","shlok","Vishruti"]

unique_list=unique_names(name_list)

print(f"List after removing duplicates is:\n {unique_list}")

      
               
                
                
        
        