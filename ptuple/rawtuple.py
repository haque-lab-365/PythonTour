# Empty tuple
empty_tuple = ()

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(type(tuple_1))
print(type(tuple_2))

print(tuple_1)
print(tuple_2)

# A one-element tuple
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

print(one_element_tuple_1)
print(one_element_tuple_2)


# Accessing tupes
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# - Not possible 
# my_tuple.append(1) # The similarities may be misleading - don't try to modify a tuple's contents! It's not a list!

var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

print(t1 + t2 + t3)
t1, t2, t3 = t2, t3, t1 
print(t1, t2, t3)


my_tuple = (1, 10, 100)
print(my_tuple)
print(len(my_tuple))

t1 = my_tuple + (1000, 10000) # concatenate 
print(t1)
print(len(t1))

t2 = my_tuple * 3
print(t2)
print(len(t2))

print(10 in my_tuple)       # True
print(-10 not in my_tuple)  # True