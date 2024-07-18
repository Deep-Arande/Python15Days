#Given two dictionaries, merge them into a single
#dictionary


#code

dic1={
     
     "name":"Deep",
     "Year":2004,
     "Age":20   
} 

dic2={
    
    "fruit":"mango",
    "weight":85,
    56:"height"
}

print(f"Dictionaries before combining:")
print(f"{dic1}\n{dic2}")

dic3=dict(dic1)
dic3.update(dic2)

print(f"Dictionaries after combining:")
print(dic3)



