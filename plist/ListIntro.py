
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




## The device records the air temperature on an hourly basis and does it throughout the month. 
## This gives you a total of 24 × 31 = 744 values.

## Initially the whole matrix is filled with zeors -  just think like default value added by device
temps = [[0.0 for h in range(24)] for d in range(31)] # h for hour and d for day
## print(temps)
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


# Three dimensional arrays | list
# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. 
# There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

ROOMS = 5
FLOORS = 5
BUILDINGS = 3

rooms = [r+1 for r in range(ROOMS)]
floors = [f+1 for f in range(FLOORS)]
building = [b+1 for b in range(BUILDINGS)]

#print(rooms_20)
#print(floors_15)
#print(building_5)


floor_vs_rooms = [rooms for f in range(FLOORS)]
floor_vs_rooms_vs_building = [floor_vs_rooms for fr in range(BUILDINGS)]
#print(floor_vs_rooms)
#print(floor_vs_rooms_vs_building)


hotels= [[['F' for r in range(ROOMS)] for f in range(FLOORS)] for t in range(BUILDINGS)]
#print(hotels)

rrm = 0
flr = 0
bld = 0


for rooms in hotels:
    rrm += 1
    print(f'R|{rrm}-{rooms}')
    for floors in rooms:
        flr += 1
        print(f'F|{flr}-{floors}')
        for buildings in floors:
            bld += 1
            # print(f'X [{rrm}]-[{rooms}], [{flr}]-[{floors}] [{bld}]- [{building}]')
            print(f'B|{bld}-{building}')
        print()
    print()



rooms= [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.

# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:

rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(f'The vacancy number is: {vacancy}')

"""

i = 2
while i >=0:
    print("*")
    i -= 2

for i in range(-1, 1):
    print("#")

z = 10
y = 0
x = z > y or z == y

print(x)

my_list = [3,1,-1]
my_list[-1] = my_list[-2]
print(my_list)

nums = []
vals = nums[:]
vals.append(1)

print(len(nums), len(vals))

data_list = [0 for i in range(1, 3)]
print(data_list)

llist = [0,1,2,3]
x = 1
for elem in llist:
    x *= elem

print(x)
