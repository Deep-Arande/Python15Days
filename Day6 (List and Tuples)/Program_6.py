# Write a Python program to count the occurrences of each
# element in a given list


# function to count the occurence of each element

def count_occurence(n_list):

    frequency = list()
    unique = list()

    for i in range(len(n_list)):

        count = 1
        if n_list[i] not in unique:
            for j in range(i+1, len(n_list)):

                if n_list[i] == n_list[j]:

                    count = count+1
            unique.append(n_list[i])
            frequency.append(count)
        else:
            frequency.append(0)

    return frequency

# code


n_list = [23, 44, 55, 63, 23, 63, 55, 63, 44, 1, 78, 23, 44, 63, 78, 55]

frequency = count_occurence(n_list)

for i in range(len(frequency)):

    if frequency[i] != 0:
        print(f"The element {n_list[i]} occurs {frequency[i]} times.")
