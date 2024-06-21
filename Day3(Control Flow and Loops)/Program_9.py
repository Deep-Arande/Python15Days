#Given a list of words, count the number of words with
#more than five characters


#function definition to count the words 

def count_word(w_list):
    
    
    count=0
    
    for i in w_list:
        
        if(len(i)>5):
            count=count+1
        
    return count

#code to take input

word_list=list()

n=int(input("Enter the number of words in the List: "))

for i in range(n):
    
    word=str(input(f"Enter the word [{i+1}]: "))
    
    word_list.append(word)
    
    
count=count_word(word_list)

print(f"The number of words with character greater than five is: {count}")


