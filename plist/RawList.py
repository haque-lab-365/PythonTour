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

"""

data_sheet = [200, 300, 50, 10, 100, 150, 300]
new_data_sheet = data_sheet[ : ]
print(f'The new data sheet is here: {new_data_sheet}')


mylist = [3,1,-1]
mylist[-1] = mylist[-2]
print(mylist)

"""
nums = []
vals = nums
vals.append(1)
print(len(nums), len(vals))


nums = []
vals = nums[:]
vals.append(1)
print(len(nums), len(vals))

ls = [0 for i in range(1,3)]
print(ls)

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]

print(s)

"""

var = 0
while var < 5:
    var +=1
    if var % 2 == 0:
        continue
    print("#")

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)


glist = [1,2,3,4,]
print(glist[-3:-2])

i = 0
while i <= 3:
    i += 2
    print("*")

lst = [i for i in range(-1,2)]
print(lst)

the_list = [1,2,3]
for v in range(len(the_list)) :
    the_list.insert(1, the_list[v])
print(the_list)


var = 1
while var < 10 :
    print("#")
    var = var << 1

x = 1
x = x == x
print(x)

lost_list = [3, 2, -1]
print(lost_list[lost_list[-1]])


cute_list = [[0,1,2,3] for i in range(2)]
print(cute_list)
#print(cute_list[2][0])

'''
i = 1
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

'''

llst_1 = [1,2,3]
llst_2 = []

for v in llst_1:
    llst_2.insert(0,v)
print(llst_2)


for i in range(1):
    print("#")
else:
    print("#")


vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

#nums = [1,2,3]
#vals = nums
#del vals[1:2]
#print(nums, vals)

nums = [1,2,3] # are nums and vals of same lenght. What are the, nums and vals are different list? analyse a lot.
vals = nums[-1:-2]
print(nums, vals)
