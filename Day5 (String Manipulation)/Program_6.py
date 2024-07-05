# Write a Python program to find the length of the longest
# word in a sentence

# function definition to find longest word

def longest_word(sentence):

    max = str(' ')
    # using split function to split string into list

    list_word = sentence.split(' ')

    for i in list_word:

        if len(max) < len(i):
            max = i

    return max

# code


sentence = str(input("Enter the sentence: "))

longest = longest_word(sentence)

print(f"The longest word in the given sentence is: {longest}")
