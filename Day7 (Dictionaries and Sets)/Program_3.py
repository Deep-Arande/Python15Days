# Implement a function that removes a key-value pair from
#a dictionary


#function to key-value pair

def remove_kv(data,key):
    
      if key in data.keys():
          data.pop(key)
          return True
      else:
          return False

#code

dic1={
    
    "name":"Deep",
    "age":20,
    "height":195
}


if(remove_kv(dic1,"name")):
    print("Key-Value pair removed.")
    print(dic1)
else:
    print("Key-Value pair doesn't exist.")