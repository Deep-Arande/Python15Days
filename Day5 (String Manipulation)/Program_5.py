# Given a string, write a function to remove all vowels from
# it and return the modified string


# function to remove vowels from a string

def remove_vowel(str1):

    r_string = str()

    for i in range(len(str1)):

        if (not (str1[i] == 'a' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u' or str1[i] == 'e' or str1[i] == 'A' or str1[i] == 'E' or str1[i] == 'I' or str1[i] == 'O' or str1[i] == 'U')):

            r_string = r_string+str1[i]


    return r_string


st=str(input("Enter the string: "))

result_str=remove_vowel(st)

print(f"The resulted string is: {result_str}")