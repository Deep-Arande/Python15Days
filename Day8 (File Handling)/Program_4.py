# Create a function that takes a list of sentences and writes 
#them to a new text file, each on a new line


#function to take list of sentence

def sentence_list(s_list):
    
    file_content=str()
    
    for i in s_list:
        file_content+=f"{i}\n"
    
    with open("program4_file.txt","w") as p_file:
        
        p_file.write(file_content)

#code

s_list=["I am a good boy","I live in Kolhapur","I like computer science and maths","Business knowledge also required to become a good engineer"]

sentence_list(s_list.copy())