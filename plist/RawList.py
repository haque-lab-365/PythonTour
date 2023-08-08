"""
numbers = [10, 9, 12, 13, 14, 15, -1]
print(numbers[1])

length = len(numbers)

numbers[0] = 111
numbers[0] = numbers[6]
print(numbers[0])
print(f'The lenght of the array is: {len(numbers)}')
del numbers[0]
print(numbers)
print(f'The lenght of the array after deleting one first index item is : {len(numbers)}')
###
# https://codetuts.dev/remove-multiple-elements-from-array-python
# Deleting multiple items from array.


numbers = [10, 9, 12, 13, 14, 15, -1]
length = len(numbers)
print("The length")

for i in range(length // 2):
    
    print(numbers[i], numbers[length - i - 1]) 
    numbers[i], numbers[length - i - 1] = numbers[length - i - 1], numbers[i]

print(numbers)



lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
print(lst)
del lst[0]
print(lst)
lst.append(1)
print(lst)




lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)




lst = [10, 20, 2, 5, 9, 7,15,6, 11, 17]
blength = len(lst)

for i in range(blength // 2):
    lst[i], lst[blength-i-1] = lst[blength-i-1], lst[i]

print(lst)

"""


my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input(f"You will enter {num} element(s). Enter list element {i + 1}: "))
    my_list.append(val)

print("The length of the array is:", len(my_list))
print(my_list)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)