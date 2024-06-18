# Create a program that takes a sentence as input and
#counts the number of words in it

sentence=str(input("Enter the sentence: "))

word=1
for i in range(0,len(sentence),1):
    
    if(sentence[i]==' '):
        word=word+1
        

print(f"The number of words in entered sentence is: {word}")