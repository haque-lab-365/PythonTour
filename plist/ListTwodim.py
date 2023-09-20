
# a 3X4 columns matrix (3 rows and 4 colums) | A two dimensional array
# https://projecteuler.net/problem=1
# https://www.codingem.com/diamond-pattern-in-python-using-for-loop/

table = [
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [0, 0, 0, 0],
        ]


'''
for td in table:
    print(" ")
    for ele in td:
        print(ele, end="  ")



for i in range(1, 10):
    ele = ("X" * i).rjust(10," ") 
    print(ele)

'''
height = 10
for i in range(height):
    print("   " * (height - i), " X " * (2 * i + 1))

for i in range(height - 1, -1, -1):
    print(" " * (height - i), " X " * (2 * i + 1))