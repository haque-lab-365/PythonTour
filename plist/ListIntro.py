
import random

# Declare empty list, fill item manually and ge the length
list_data = []
print(f'The lenght of the lis is: {len(list_data)}')
list_data = [1]
print(f'The lenght of the lis is: {len(list_data)}')
list_data = [10, 20, 13, 15, 11, 14, 19, 17, 16, 18]
print(f'The lenght of the lis is: {len(list_data)}')

print(f'The data type of the list is:{type(list_data)}')


vowel_list_5 = ["A", "E", "I", "O", "U"]
consonant_list_21 = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

print(f'Choice one vowel randomly: {random.choice(vowel_list_5)}')
print(f'Choice three consonant randomly: {random.sample(consonant_list_21,3)}')

"""
Multidimensional nature of lists: advanced applications
Let's go deeper into the multidimensional nature of lists. To find any element of a two-dimensional list, you have to use two coordinates:

a vertical one (row number)
and a horizontal one (column number).
Imagine that you develop a piece of software for an automatic weather station. The device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

"""


# The device records the air temperature on an hourly basis and does it throughout the month. 
# This gives you a total of 24 × 31 = 744 values.

# Initially the whole matrix is filled with zeors -  just think like default value added by device
temps = [[0.0 for h in range(24)] for d in range(31)] # h for hour and d for day
#print(temps)
highest = -100.0
total = 0.0
i = 0

for day in temps:
    i += 1
    print(f'{i}{day}')
    total += day[11]

average = total / 31
print("Average temperature at noon:", average)

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
            
print("The highest temperature was:", highest)