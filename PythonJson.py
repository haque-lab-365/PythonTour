import json

jsndata = '{"Name": "John", "age":30, "City": "New York", "ID": "11100110011"}' 
y = json.loads(jsndata)
print(y)

#The resutl is a python dictionary

print(y["Name"])


# Convert from python to json
pobject = {
    "name": "John",
    "age" : 30,
    "City": "New Yourk"
}

# Convert into json
convertedJson = json.dumps(pobject)
print(convertedJson)

# We can convert Python objects of the following types, into JSON strings: [dict,list,tuple,string,int,float,True,False,None]
# Let's Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name":"John",  "age":30}))       # Dictionary
print(json.dumps(["Apple", "Bananas", "Orange"]))   # List
print(json.dumps(("Apple", "Bananas", "Orange")))   # Tuples
print(json.dumps("Hello World!")) # String datatype 
print(json.dumps(42)) # Integer
print(json.dumps(100.20)) # Decimal
print(json.dumps(True)) # Boolean True
print(json.dumps(False)) # Boolean Fals.
print(json.dumps(None)) # null??


# Let's convert a Python object containing all the legal data types:

alldt = {
    "name": "Shahidul",
    "age": 45,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Bill"),
    "childre_age" : [4,10],
    "pets": None,
    "cars": [
        {"model": "BMW-230", "mpg":27.5},
        {"model": "Ford-Edge", "mpg":24.1}
    ]
}

print(json.dumps(alldt))
#print(json.dumps(alldt, indent=4))
print(json.dumps(alldt, indent=4, sort_keys=True))
