
# Declaring a list with content || List is created using square brackets:

# Empty new list:
empty_new_list = [] # No content is there, lenth is zero.


# ListName = [(0)ListItem0, (1)ListItem1, (2)ListItem2, (3)ListItem3, (n)ListItem..n...]
emp_identity = [1, 2, 3, 4, 5]
emp_names = ["Marks", "Tom", "Fuda", "Alex", "Cruz"]
emp_score = [-5, -6, -3, -7, -2]
emp_salary = [3000.75, 40000.00, 3000.75, 35000.60, 50000.22]
emp_cars = [True, False, False, True, False] # List with boolean values.


diff_data_types_list = [False, True, 1, "Hello", 3.4, 'Good']
dup_list_items = [1, 1, True, True,  "Hello", 3.4, "Hello", 3.4, 500] 


# Constructor based list creation:
thislist = list(("Cars", "Bikes", "Trains", "Ships")) # double round-brackets makes a constructor.
print(thislist)


# Accessing list items 


# @@ When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# @@ If you add new items to a list, the new items will be placed at the end of the list.
# @@ The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# @@ Since lists are indexed, lists can have items with the same value
# @@ List items can be of any data type
# @@ Complexities for Creating Lists : Time Complexity: O(1) Space Complexity: O(n)
