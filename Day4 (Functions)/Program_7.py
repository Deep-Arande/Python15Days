# Create a function that takes a list of strings and returns
# the list sorted alphabetically


# function definition to sort string list
def sort_list(s_list):

    return sorted(s_list)

#code
s_list = list()
n = int(input("Enter the number of elements in list: "))

for i in range(n):

    st = str(input(f"Enter the string [{i+1}]: "))
    s_list.append(st)

st_list = sort_list(s_list)

print(f"List after sorting:\n{st_list}")
