#Given a list of dictionaries, find the dictionary with the
#highest value for a specific key 

#function to return dictionary with highest value of specified key

def high_value(data_list,key):
    
    max=data_list[0][key]
    r_dict=data_list[0]
    for data in data_list:
        
        if max<data[key]:
            max=data[key]
            r_dict=data
        
    return r_dict
        

#code
#list of dictionaries
d_list=[
    
    {
        "name":"Deep",
        "Age":20
    },
    
    {
        "name":"Harshada",
        "Age":65
    },
    
    {
        
        "name":"Dog",
        "Age":45
    }
]

r_dict=high_value(d_list,"Age")

print(f"The dictionary with highest value of specified key is:\n {r_dict}")