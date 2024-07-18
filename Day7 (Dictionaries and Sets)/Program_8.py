#Create a function that takes a list of dictionaries and sorts
#them based on a specified key


#Function to take list of dictionaries

def sort_dict(l_dict,key):
    
    s_dict=list()
    
    while(l_dict):
        
        small=0
        for j in range(len(l_dict)):
            
            if l_dict[small][key]> l_dict[j][key]:
                
                small=j
        
        s_dict.append(l_dict[small])
        l_dict.pop(small)
        
    
    return s_dict


#code

k_dict=[
    
    {"name":"Deep","age":20},
    {"name":"Akshay","age":30},
    {"name":"Rohit","age":25},
    {"name":"Sarthak","age":12},
]
    
    
sr_dict=sort_dict(k_dict.copy(),"age")

print(f"Dictionary after sorting using key \"age\":\n")

print(k_dict)

    
        
        
    
    