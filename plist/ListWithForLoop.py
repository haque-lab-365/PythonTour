
#from PythonDataList import *
from plist.ListData import*


winterSeasonFruits_10 = winterSeasonFruitlist[:10]
springSeasonFruits_10 = springSeasonFruitList[:10]
summerSeasonFruits_10 = summerSeasonFruitList[:10]
fallSeasonFruits_10 = fallSeasonFruitList[:10]

## Loop through the list: iterate winter season fruite list | 
print("Loop through the list-iterate with for and in keyword")

print("-----------Winter Season Fruit List-----------\n\n")
for wsf in winterSeasonFruits_10:
    print(wsf)

print("-----------Spring Season Fruit List-----------\n\n")
for ssf in springSeasonFruits_10:
    print(ssf)

print("-----------Summer Season Fruit List-----------\n\n")
for ssfl in summerSeasonFruits_10:
    print(ssfl)

print("-----------Fall Season Fruit List-----------\n\n")
for fsf in fallSeasonFruits_10:
    print(fsf)

print("Loop Through the Index Numbers")

for i in range(len(winterSeasonFruitlist)):
    print(f'The winter season fruit list - comes with loop in index number {i}: content: {winterSeasonFruitlist[i]}')
for j in range(len(springSeasonFruitList)):
    print(f'The Spring Season Fruit List - comes with loop in index number {j}: content: {springSeasonFruitList[j]}')
for k in range(len(summerSeasonFruitList)):
    print(f'The Summer Season Fruit List - comes with loop in index number {k}: content: {springSeasonFruitList[k]}')
for l in range(len(fallSeasonFruitList)):
    print(f'The Fall Season Fruit List - comes with loop in index number {l}: content: {springSeasonFruitList[l]}')


print(f'Looping Using List Comprehension')

#The below code is very expensive
#[print(f'Item-WSFL:{a},Item-SSFL:{b},Item-SSFL(*):{c},Item-FSFL: {d}') for a in winterSeasonFruitlist for b in springSeasonFruitList for c in summerSeasonFruitList for d in fallSeasonFruitList]
