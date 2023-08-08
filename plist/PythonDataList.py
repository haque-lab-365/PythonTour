from plist.ListData import *
import datetime

# Declaring a new empty list in python.
newList = []
newChunk = []

today = datetime.datetime.today()


print("The type of all lists is printed below:")
print (type(winterSeasonFruitlist), type(springSeasonFruitList), type(summerSeasonFruitList), type(fallSeasonFruitList))

print("The length of all lists is printed below:")
#print('winterSeasonFruitlist: '+ len(winterSeasonFruitlist), 'springSeasonFruitList :' + len(springSeasonFruitList), 'summerSeasonFruitList :' + len(summerSeasonFruitList), 'fallSeasonFruitList :' + len(fallSeasonFruitList))

# Using f-strings
winterFruits = 'Winter Season Fruit List'
springFruits = 'Spring Season Fruit List'
summerFruits = 'Summer Season Fruit List'
fallFruits = 'Fall Season Fruit List'


print(f"Hello, The length of  {winterFruits} is: {len(winterSeasonFruitlist)}, including zero index.")
print(f"Hello, The length of  {springFruits} is: {len(springSeasonFruitList)}, including zero index.")
print(f"Hello, The length of  {summerFruits} is: {len(summerSeasonFruitList)}, including zero index.")
print(f"Hello, The length of  {fallFruits} is: {len(fallSeasonFruitList)}, including zero index.")


# Accessing list items - using positive index
if len(winterSeasonFruitlist) > 0:
    print(f'The first items is {winterSeasonFruitlist[0]} -  I like it!')

if len(springSeasonFruitList) > 0:
    print(f'The first items is {springSeasonFruitList[0]} -  I don not like it!')

if len(summerSeasonFruitList) > 0:
    print(f'The first items is {summerSeasonFruitList[0]} -  Everybody likes it!')

if len(fallSeasonFruitList) > 0:
    print(f'The first items is {fallSeasonFruitList[0]} -  No body dislikes it!')

# Accessing list items - using nvegative index | Negative indexing means start from the list end|  -1 refers to the last item, -2 refers to the second last item etc.
print("ACCESSING LIST ITEMS FROM THE LIST END") 

if len(winterSeasonFruitlist) > 0:
    print(f'The last items is {winterSeasonFruitlist[-1]} -  I like it!')

if len(springSeasonFruitList) > 0:
    print(f'The second last items is {springSeasonFruitList[-2]} -  I don not like it!')

if len(summerSeasonFruitList) > 0:
    print(f'The third last items is {summerSeasonFruitList[-3]} -  Everybody likes it!')

if len(fallSeasonFruitList) > 0:
    print(f'The fourth last items is {fallSeasonFruitList[-4]} -  No body dislikes it!')

# Accessing list items - with Range of Indexes
print("ACCESSING LIST ITEMS Within range \n\n") 

if len(winterSeasonFruitlist) > 0:
    print(f'Give me some winter fruits: {winterSeasonFruitlist[2:5]}-I like these fruits!')
    #["Chestnuts","Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
    # Outputs: "Lemons","Oranges","Tangerines"
if len(springSeasonFruitList) > 0:
    print(f'Give me some spring fruits: {springSeasonFruitList[2:5]}-We don not like these fruits!')
    #-["Apricots","Avocado","Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
    # Outputs: "Mango","Pineapple","Rhubarb"   
if len(summerSeasonFruitList) > 0:
    print(f'Give me some summer fruits: {summerSeasonFruitList[2:5]}-Everybody likes these fruits!')
    #["Blackberries","Blueberries","Nectarines","Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]
    # Outputs: "Mango","Pineapple","Rhubarb"   
if len(fallSeasonFruitList) > 0:
    print(f'Give me some fall season fruits: {fallSeasonFruitList[2:5]} -  No body dislikes these fruits!')
    # ["Apples","Cranberries","Figs","Grapes","Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]
    # Outputs: "Mango","Pineapple","Rhubarb"   



# Accessing list items - with Range of Indexes
print("ACCESSING LIST ITEMS using RANGE without START value \n\n") 

if len(winterSeasonFruitlist) > 0:
    print(f'Give me 2 winter fruits: {winterSeasonFruitlist[:2]}-I like these fruits!')
    #["Chestnuts","Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
    # Outputs: ["Chestnuts","Grapefruit"]
if len(springSeasonFruitList) > 0:
    print(f'Give me 3 spring fruits: {springSeasonFruitList[:3]}-We don not like these fruits!')
    #-["Apricots","Avocado","Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
    # Outputs: ["Apricots","Avocado","Mango"]
if len(summerSeasonFruitList) > 0:
    print(f'Give me 4 summer fruits: {summerSeasonFruitList[:4]}-Everybody likes these fruits!')
    #["Blackberries","Blueberries","Nectarines","Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]
    # Outputs: ["Blackberries","Blueberries","Nectarines","Peaches"]   
if len(fallSeasonFruitList) > 0:
    print(f'Give me 5 fall season fruits: {fallSeasonFruitList[:5]}-No body dislikes these fruits!')
    # ["Apples","Cranberries","Figs","Grapes","Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]
    # Outputs: ["Apples","Cranberries","Figs","Grapes","Pears"]   


# Accessing list items - with Range of Indexes
print("ACCESSING LIST ITEMS using RANGE without END value \n\n") 

if len(winterSeasonFruitlist) > 0:
    print(f'Skip chestnuts: {winterSeasonFruitlist[1:]}-I like these fruits!')
    #["Chestnuts","Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
    # Outputs: ["Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
if len(springSeasonFruitList) > 0:
    print(f'Skipp two fruits fruits: {springSeasonFruitList[2:]}-We don not like these fruits!')
    #-["Apricots","Avocado","Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
    # Outputs: ["Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
if len(summerSeasonFruitList) > 0:
    print(f'Skip three fruits: {summerSeasonFruitList[3:]}-Everybody likes these fruits!')
    #["Blackberries","Blueberries","Nectarines","Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]
    # Outputs: ["Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]   
if len(fallSeasonFruitList) > 0:
    print(f'Skip four fruits: {fallSeasonFruitList[4:]}-No body dislikes these fruits!')
    # ["Apples","Cranberries","Figs","Grapes","Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]
    # Outputs: ["Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]

print("RANGE of NEGATIVE INDEXES \n\n")

if len(winterSeasonFruitlist) > 0:
    print(f'Negaiteve index: {winterSeasonFruitlist[-4:-1]}-I like these fruits!')
    #["Chestnuts","Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
    # Outputs: ["Radicchio","Radishes","Rutabaga"]
if len(springSeasonFruitList) > 0:
    print(f'Give me some beans: {springSeasonFruitList[-5:-2]}-We don not like these fruits!')
    #-["Apricots","Avocado","Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
    # Outputs: ["Fava Beans","Fennel","Fiddlehead Ferns"]
if len(summerSeasonFruitList) > 0:
    print(f'Grab Tomato, Water melon and Broccoli: {summerSeasonFruitList[-6:-3]}-Everybody likes these fruits!')
    #["Blackberries","Blueberries","Nectarines","Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]
    # Outputs: ["Tomatoes","Watermelon","Broccoli"]   
if len(fallSeasonFruitList) > 0:
    print(f'Grab garlic, Ginger and Mashroom : {fallSeasonFruitList[-7:-4]}-No body dislikes these fruits!')
    # ["Apples","Cranberries","Figs","Grapes","Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]
    # Outputs: ["Garlic","Ginger","Mushrooms"]


print("CHECK IF ITEM EXISTS: \n\n")
print("To determine if a specified item is present in a list use the <<in>> keyword")


if len(winterSeasonFruitlist) > 0:
    #["Chestnuts","Grapefruit","Lemons","Oranges","Tangerines","Kale","Leeks","Radicchio","Radishes","Rutabaga","Turnips"]
    if "Grapefruit" in winterSeasonFruitlist:
        print(f' The index of <Grapefruit> is: {winterSeasonFruitlist.index("Grapefruit")}')

if len(springSeasonFruitList) > 0:
    #-["Apricots","Avocado","Mango","Pineapple","Rhubarb","Strawberries","Artichoke","Asparagus","Carrots","Celeriac","Chives","Collards","Fava Beans","Fennel","Fiddlehead Ferns","Morels","Mustard Greens"]
    if "Mango" in springSeasonFruitList:
        print(f' The index of <Mango> is: {springSeasonFruitList.index("Mango")}')

if len(summerSeasonFruitList) > 0:
    #["Blackberries","Blueberries","Nectarines","Peaches","Plums","Raspberries","Tomatoes","Watermelon","Broccoli","Cucumber","Green Beans","Zucchini"]
    if "Peaches" in summerSeasonFruitList:
        print(f'The index of <Peaches> is: {summerSeasonFruitList.index("Peaches")}')

if len(fallSeasonFruitList) > 0:
    # ["Apples","Cranberries","Figs","Grapes","Pears","Pomegranate","Quince","Butternut Squash","Cauliflower","Garlic","Ginger","Mushrooms","Potatoes","Pumpkin","Sweet Potatoes","Swiss Chard"]
    if "Pears" in fallSeasonFruitList:
        print(f' The index of <Pears> is: {fallSeasonFruitList.index("Pears")}')




#https://www.digitalocean.com/community/tutorials/python-concatenate-string-and-int
#https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
      
   


# Example 1: How to create a nested dictionary
# https://www.programiz.com/python-programming/nested-dictionary

'''
genemplyees = {
                    1: {'name': 'Abdullah Rashel', 'Email':'rashel.abdullah@genweb2.com', 'Role': 'Member', 'JoiningDate':'Jun 22,2021'},
                    2: {'name': 'Tahmidul Abedin', 'Email':'abedin.tahmidul@genweb2.com', 'Role': 'Member', 'JoiningDate': 'Jan 1,2017'},
		            3: {'name': 'Adnan Bin Zahir', 'Email':'zahir.adnan@genweb2.com', 'Role': 'Member', 'JoiningDate': 'Feb 14, 2022'},
		            4: {'name': 'Shafath Ahmed', 'Email':'ahmed.shafath@genweb2.com', 'Role': 'Member', 'JoiningDate': 'Dec 21, 2016'},
                    5: {'name': 'Akther Ahmed', 'Email':'akthera@genweb2.com', 'Role': 'Chairman', 'JoiningDate': 'Feb 14, 2022'},
                    6: {'name': 'Jobaidul Alam', 'Email':'alam.jobaidul@genweb2.com', 'Role': 'Member', 'JoiningDate': 'Jun 21, 2016'},
                    7: {'name': 'Rashedul Alam', 'Email':'alam.rashedul@genweb2.com', 'Role': 'Member', 'JoiningDate': 'Jul 14, 2015'},
                    8: {'name': 'Ahmed Sifat', 'Email':'sifat.ahmed@genweb2.com', 'Role': 'Member', 'JoiningDate': 'May 8, 2022'}
              }

print(genemplyees)

print(genemplyees[1]['name'])
print(genemplyees[1]['Email'])
print(genemplyees[1]['Role'])
print(genemplyees[1]['JoiningDate'])

'''