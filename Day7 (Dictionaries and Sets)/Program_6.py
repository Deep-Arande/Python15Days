# Write a Python program that counts the number of
# occurrences of each character in a given string using a
# dictionary


# function to count occurence of each character

def count_occurence(str1):

    count = dict()

    for i in str1:

        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count

# code


n_str = str(input("Enter the string: "))


char_count = dict(count_occurence(n_str))

print(f"Count of each character in string {n_str} is:")
for i in char_count.keys():

    if i != ' ': #condition to avoid white-space
        print(f"{i}:{char_count[i]}")
