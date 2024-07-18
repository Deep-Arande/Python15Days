# Write a program that finds the most frequent element in a
# list

# we will create a function that creates dictionaries to store occurence of element

def store_occurence(n_list):

    occur = dict()

    for i in n_list:

        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1

    return occur


# list to store integers
n_list = [2, 3, 4, 7, 1, 56, 2, 3, 3, 3, 3, 78, 51, 34, 18, 43, 22, 78, 51, 78]

frequency = store_occurence(n_list)

# varible to store most occured element

max = int()
freq = int(1)  # variable to update frequency of the occurence

for i, j in frequency.items():

    if freq < j:
        max = i
        freq = j

print(f"The most occured element is {max} with frequency {freq}")