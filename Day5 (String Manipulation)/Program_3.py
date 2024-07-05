# Create a program that takes a sentence as input and
# counts the number of words in it


# function definition to count the words in a string

def count_word(sentence):
    word = 1
    start=0
    i=0
    #loop to bypass starting white-spaces
    
    while(sentence[i] == ' '):
        start=start+1
        i=i+1

    for i in range(start, len(sentence), 1):

        if (sentence[i] == ' '):
            word = word+1

    return word
sentence = str(input("Enter the sentence: "))

word=count_word(sentence)
print(f"The number of words in entered sentence is: {word}")
