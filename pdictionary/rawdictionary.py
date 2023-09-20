

'''
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dtlist = [10, 20, 30, 40, 50]
tplist = (11, 22, 33, 44, 55)
tplist1 = 12.5, 24.5, 36.5, 46.10

dictdata = {"cat":"cha", "dog": "chien", "horse": "cheval"}
print(dictdata)

hundred_eng_fr_dic = {
                        "time":"temps",
                        "year":"année",
                        "people":"personnes",
                        "way":"chemin",
                        "day":"jour",
                        "man":"homme",
                        "thing":"chose",
                        "woman":"femme",
                        "life":"vie",
                        "child":"enfant",
                        "world":"monde",
                        "school":"école",
                        "state":"État",
                        "family":"famille",
                        "student":"étudiant",
                        "group":"groupe",
                        "country":"pays",
                        "problem":"problème",
                        "hand":"main",
                        "part":"partie",
                        "place":"lieu",
                        "case":"cas",
                        "week":"semaine",
                        "company":"entreprise",
                        "system":"système",
                        "program":"programme",
                        "question":"question",
                        "work":"travail",
                        "governme":"gouvernement",
                        "number":"nombre",
                        "night":"nuit",
                        "point":"indiquer",
                        "home":"maison",
                        "water":"eau",
                        "room":"chambre",
                        "mother":"mère",
                        "area":"zone",
                        "money":"argent",
                        "story":"histoire",
                        "fact":"fait",
                        "month":"mois",
                        "lot":"parcelle",
                        "right":"droite",
                        "study":"étude",
                        "book":"livre",
                        "eye":"œil",
                        "job":"emploi",
                        "word":"mot",
                        "business":"entreprise",
                        "issue":"problème",
                        "side":"côté",
                        "kind":"gentil",
                        "head":"tête",
                        "house":"maison",
                        "service":"service",
                        "friend":"ami",
                        "father":"père",
                        "power":"pouvoir",
                        "hour":"heure",
                        "game":"jeu",
                        "line":"doubler",
                        "end":"fin",
                        "member":"membre",
                        "law":"loi",
                        "car":"voiture",
                        "city":"ville",
                        "communit":"communautaire",
                        "name":"nom",
                        "presiden":"présidente",
                        "team":"équipe",
                        "minute":"minute",
                        "idea":"idée",
                        "kid":"enfant",
                        "body":"corps",
                        "informat":"informat",
                        "back":"dos",
                        "parent":"parent",
                        "face":"affronter",
                        "others":"autres",
                        "level":"niveau",
                        "office":"bureau",
                        "door":"porte",
                        "health":"santé",
                        "person":"personne",
                        "art":"art",
                        "war":"guerre",
                        "history":"histoire",
                        "party":"faire la fête",
                        "result":"résultat",
                        "change":"changement",
                        "morning":"matin",
                        "reason":"raison",
                        "research":"recherche",
                        "girl":"fille",
                        "guy":"gars",
                        "moment":"moment",
                        "air":"air",
                        "teacher":"professeur",
                        "force":"forcer",
                        "ducation":"ducation"
                    }

#print(hundred_eng_fr_dic) 

words = ['cat', 'dog', 'time', 'man', 'friend','head', 'ducation']

for word in words:
    if word in hundred_eng_fr_dic:
        print(word, "|En:--> Fr: ", hundred_eng_fr_dic[word])
    else:
        print(word, "is not in dictionary")

print("Accessing dictionary with keys...")

for key in sorted(hundred_eng_fr_dic.keys()):
    print(f'The English word {key} means {hundred_eng_fr_dic[key]} in French')


print("Accessing dictionary with items (key  and value)...")

for english, french in hundred_eng_fr_dic.items():
    print(f' Different way: The English word {english} means {french} in French')


print("Access only values from the dictionary")
for french in hundred_eng_fr_dic.values():
    print(french)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


dictionary['rat'] = 'Grrr...'
print(dictionary)

dictionary['cow'] = 'Good'
print(dictionary)

dictionary.update({"duck": "canard", "hen": "kok"})
print(dictionary)

#del dictionary['rat']
#print(dictionary)

dictionary.popitem()
print(dictionary)


school_class = {}

while True:

    name = input("Enter the students name: ")
    if name == "":
        break 

    score = int(input("Enter the student's score(0 - 10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score, )
    else:
        school_class[name] = (score, )

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0

    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

'''

from random import randrange
for i in range(10):
    print(randrange(8))


for i in range(5):
    for j in range(10):
        print("+-------+", end=" ")
        print(i)
        print("+-------+", end=" ")
    
    print()


val1 = input(print("Enter value"))
b = len(val1) * 2
print(b)
            


