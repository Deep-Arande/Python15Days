# Create a function that takes a list of strings and returns
# the list sorted by the length of the strings


# function to sort the list

def sort_str(str_list):

    list1 = str_list
    sort_list = list()

    while (list1):

        small = list1[0]
        small_index = 0
        for i in range(len(list1)):

            if len(small) > len(list1[i]):
                small = list1[i]
                small_index = i

        sort_list.append(small)
        list1.pop(small_index)

    return sort_list


# code

str_list = ["Kedar", "Deep", "Akshay", "Om", "Jay", "Shatakshi", "Abi", "manu"]


r_list = sort_str(str_list)

print(f"List after sorting:\n {r_list}")
