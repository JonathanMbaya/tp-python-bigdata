populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]



from random import randint, choice

ALEA = 100
NUMBER_POPULATION = len(populations)

# 1. Ajoutez un champ **lenChar** qui détermine la longueur de chaque nom.

for pop in populations:
    pop['lenChar'] = len(pop['name'])

# 1. Ajoutez un champ rate, puis respectivement attribuer pour chaque personne, des valeurs aléatoires comprises entre 1 et 100.    

for pop in populations:
   pop['rate'] = randint(1, ALEA)
   
# 1. Déterminez les 4 personnes qui ont les meilleurs valeurs de rate.

populations = sorted( populations, key=lambda p : p['rate'], reverse=True )

# print(populations[:4])

# 1. Attribuez une augmentation de 0.1% à chacune des valeurs ( rate ).

"""
On utilise le constructeur list pour créer une liste à partir du générateur map
"""

# populations = list( map(
#     lambda pop : { **pop, 'rate' : pop['rate']*1.01  }, 
#     populations
#     ) )

# print(populations)
# print( { **populations[0], 'rate' : 100  } )

"""
On peut garder le résultat dans le générateur pour ne pas occuper d'espace mémoire
"""
gen = map(
    lambda pop : { **pop, 'rate' : pop['rate']*1.01  }, 
    populations
    ) 

# for e in gen:
#     print(e)

# print(range(10))

# 1. Créez une fonction qui permet de tirer de manière aléatoire une personne.

def getPerson():
    return populations [ randint(0, NUMBER_POPULATION - 1) ]

"""
On peut utiliser choice du module random
"""

# print( getPerson() )
# print( choice(populations) )

# 1. Ordonnez par ordre croissant dans une liste s de tuples, les personnes en fonction de leur rate respectif.

populations = sorted( populations, key=lambda p : p['rate'], reverse=False )

s = list( map(lambda pop : ( pop['name'], pop['rate'] ), populations) )

# print(s)

# 1. Trouvez la valeur centrale, la valeur centrale partage en deux la série de valeurs rates ordonnées.

def mediane(populations):
    nb = len(populations)
    if nb % 2 :
        return populations[ nb // 2 ]["rate"]

    v =  populations[ nb // 2 ]["rate"]
    w =  populations[ (nb // 2) - 1 ]["rate"]
        
    return round( (v + w) / 2, 1 )

m =  mediane(populations) 

# 1. Partionnez la liste s en quatre parties distinctes. Que représente à votre avis la valeur centrale déterminée dans la question précédente. 

def partition(m, pop):
    q1, q2 = [], []
    for p in pop :
        if m <= p['rate'] : q1.append(p)
        else : q2.append(p)
        
    return q1, q2

# on découpe s en Q1 et Q2
Q2, Q1 = partition(m, populations)

print("Q1 ------- Q2")
print("Q1", Q1)
print("--------")
print("Q2", Q2)

# on calcule les valeurs centrales des listes Q1 et Q2
m1 = mediane(Q1)
m2 = mediane(Q2)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

# Calcule les quatre partitions à l'aide de la fonction partition
q2, q1 = partition(m1,Q1)
q4, q3 = partition(m2,Q2)

q2 = list(map(lambda p : p['rate'], q2))
q1 = list(map(lambda p : p['rate'], q1))
q4 = list(map(lambda p : p['rate'], q4))
q3 = list(map(lambda p : p['rate'], q3))

print("------", m1)
print(q1)
print("------")
print(q2)
print("------", m2)
print(q3)
print("------")
print(q4)