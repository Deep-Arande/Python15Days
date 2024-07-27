#Implement a program that reads a text file and counts the 
#number of words and lines in it

#code

with open("python_essay.txt","r") as p_file:
    
    content=p_file.readlines()


n_lines=int(len(content))
n_words=int(0)

for i in content:
    
    l_word=i.split()
   
    n_words+=len(l_word)
    
print(f"Number of lines are{n_lines}")
print(f"Number of words are{n_words}")
