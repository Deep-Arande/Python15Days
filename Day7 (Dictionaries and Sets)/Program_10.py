# Implement a function that takes a list of strings and
# returns a set of unique characters present in all strings


# function to return set of unique characters present in all string

def unique_chars(str1):

    count_dict = dict()
    word = str()  # to store characters in string that occure atleast once
    for i in str1:

        if i not in word:
            word += i
            count_dict[i] = 1
        else:
            count_dict[i] += 1

    r_char = str()  # string to return characters that occurs only once

    for i in count_dict.keys():

        if count_dict[i] == 1:
            r_char += i
    
    
    return r_char


def return_unique(s_list):

    set_list = list()  # list to store sets

    for i in s_list:

        u_set = set()
        u_set.add(unique_chars(i.lower()))  # add unique characters in set
        

        set_list.append(u_set.copy())  # add set in the list
        u_set.clear()  # clear the set to add new items
     
    return set_list


#code 

st_list=["Deep","Kedar","Banty","Akshay","Sai"]


r_list=return_unique(st_list.copy())

print("Sets with unique characters are:")

for i in r_list:
    print(f"{i}")
    