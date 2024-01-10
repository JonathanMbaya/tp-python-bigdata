students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
print('albert' in students)

#-------------------------------------------

students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
for h in map(hash, students): 
    print(h) 
"""
1623984986049861657
-2969457881634950836
8552435218161168756
"""

#-------------------------------------------

l = [('alan', 1), ('albert' ,2) , ('brice', 3) ]
lDic = dict(l)
print(lDic)

#-------------------------------------------

students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
students['alan'] = 1001
students['alan'] # 1001
print(students)
del students['alan'] # supprime cet clé/valeur
print(students.keys()) # crée une liste de clés 
print(students.values()) # crée une liste de valeurs 

#-------------------------------------------

for (k, v) in students.items():
    print(k, v)

students.items() 
# donne une liste particulière qui vient d'un dict
# dict_items([('alan', 1), ('albert', 2), ('brice', 3)])

#-------------------------------------------

# définition d'un tuple
t = 'a', 'b', 'c'
u = t, (1,2,4)
print(u)
# (('a', 'b', 'c'), (1,2,4))

#-------------------------------------------

t = ('a', 'b', 'c')
x,y,z = t
print(x,y,z)

#-------------------------------------------

languages = ['JS', 'Python', 'PHP'] 
versions = [6, 3, 8]
res = zip(languages , versions)
print(list(res))

#-------------------------------------------

#Nettoyez les données, vous retirez l'item EURO pour le prix de chaque appareil

phones = [
{ 'name': "iphone XX", 'priceHT': "900EURO" },
{ 'name': "iphone X", 'priceHT': "70EURO" },
{ 'name': "iphone B", 'priceHT': "200EURO" },
]

for phone in phones:
    phone['priceHT'] = phone['priceHT'].replace('EURO', '')

print(phones)

for phone in phones:
    print (phone)

#-------------------------------------------
    
#Faites la somme des valeurs numériques contenus dans la chaîne de caractères suivante, en utilisant les compréhension de liste

res = '1 2 3 4 5 6 7 8 9 10 11 16'
# premiere solution
# total = sum(float(v) for v in res if v != ' ')

# deuxième solution
# total = sum(float(v) for v in res.split(' ') )

# troisième solution
total = sum( map( float, res.split(' ')) )

print(total)

#-------------------------------------------

numbers = [110, 230, 200]
coeffs = [ .1, 1.5, .01 ]

res = [ x + c for x in numbers for c in coeffs ]

# dans un style impératif

res = []
for x in numbers:
    for c in coeffs :
        res.append( x + c)

print(res)

'''

Exercice 3

'''

def findSequence(l, sequence):
    len_sequence = len(sequence)
    for i in range(len(l) - len_sequence + 1):
        if l[i:i+len_sequence] == sequence:
            return i
    return -1  # Retourne -1 si la séquence n'est pas trouvée

# Exemple d'utilisation avec la liste donnée
l = [1, 3, 7, 8, 9, 1, 2, 3, 8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
sequence= [1, 2, 3, 8]

indice = findSequence(l, sequence)

if indice != -1:
    print(f"La séquence est trouvée à l'indice {indice}.")
else:
    print("La séquence n'est pas trouvée dans la liste.")
