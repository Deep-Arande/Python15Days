# Given a list of integers, find the sum of all positive
# numbers

# function to find sum of all positive numbers in a list
def sum_positive():
    n_list = list()
    sum = 0
    n = int(input("Enter the number of elements in list: "))
    for i in range(0, n, 1):

        ele = int(input(f"Enter the element [{i}]: "))

        n_list.insert(i, ele)
        if (ele >= 0):
            sum = sum+ele

    return sum

sum=sum_positive()
print(f"The sum of all positive elements in the list is: {sum}")
