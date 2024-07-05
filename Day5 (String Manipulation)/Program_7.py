#Create a function that takes a sentence as input and
#returns the sentence in reverse order


#function definition to reverse a sentence

def reverse_sent(sentence):
    
    word_list=sentence.split(' ')
    
    reverse_word=word_list[::-1]
    rev_sentence=str()
    
    for i in reverse_word:
        
        rev_sentence=rev_sentence+i+' '
        
    return rev_sentence

#code

sentence=str(input("Enter the sentence: "))

rev_sent=reverse_sent(sentence)

print(f"Sentence after reversing is:\n {rev_sent}")
