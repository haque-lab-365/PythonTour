
# Remember - Python reads your code from top to bottom. It's not going to look ahead in order to find a function you forgot to put in the right place 

def message() :
    print("Enter a value...")

print("We started here...")
message()
print("We ended here....")

# Guess what has been done here ? Fucntion named has been assinged a value as a varablie.
message = 1
print(message)

# -- Call the function again.. it will through an error.
# message() # It will throw error since its no logner a function. 

# Parameterized function
def shownumber(number) :
    print("The number is:", number)

shownumber(100)
shownumber(200)
shownumber(300)
shownumber(400)


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))