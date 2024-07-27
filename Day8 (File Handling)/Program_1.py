#Write a Python program to copy the contents of one text 
#file into another



#code


#opening file 
with open("file1.txt","r") as file1:
    
    content=file1.read()

with open("file2.txt","w") as file2:
    
    file2.write(content)