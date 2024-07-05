# Implement a program that takes a sentence and a word as
# input and checks if the word is present in the sentence


# function defintion to check above condition

def word_predent(sentence, word):

    name_list = list()

    name_list = sentence.split()

    if word in name_list:
        return True

    else:
        False

#code
sentence=str(input("Enter the sentence: "))
word=str(input("Enter the word you need to search: "))

if(word_predent(sentence,word)):
    
    print(f"The entered word is present: ")
    
else:
    print("Entered word is not present: ")