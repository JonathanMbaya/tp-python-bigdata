from random import randint



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

# Ajouter un champ lenChar qui compte le nbre de lettre

# nom = input ('')
# nomLen =  len(nom)

# print ( f"{nom} contient exactement {nomLen} de lettre(s)")


'''
Etape 1
Ajoutez un champ lenChar qui détermine la longueur de chaque nom.

'''
# Ajoutez le champ lenChar à chaque entrée du tableau
for person in populations:
    person['lenChar'] = len(person['name'])

# Affichez le tableau mis à jour
for person in populations:
    print(person)


'''
Etape 2
Ajoutez un champ rate, puis respectivement attribuer pour chaque personne, des valeurs aléatoires comprises entre 1 et 100.

'''
# Ajouter un champ rate à chaque entrée du tableau
for person in populations:
    person['rate'] = randint(1, 100)

# Afficher le tableau
for person in populations:
    print (person)

'''
Etape 3
Déterminez les 4 personnes qui ont les meilleurs valeurs de rate.

'''
# Créer un tableau en ordre décroissant
tab_order = sorted(populations,key=lambda person: person['rate'], reverse=True)

# Sélectionnez les 4 premières personnes avec les meilleures valeurs de rate
best_rate = tab_order[:4]

# Affichez les 4 personnes avec les meilleures valeurs de rate
for person in best_rate:
    print(f"{person['name']} a une valeur de rate de {person['rate']}.")


'''
Etape 4
Attribuez une augmentation de 0.1% à chacune des valeurs ( rate ).

'''

# Récupérer les valeurs de chaque rate et mulitiplier par 1,1 pour rajouter 0,1%
for person in populations:
    person['rate'] = int(person["rate"])*1.1

# Afficher le tableau
for person in populations:
    print (person)


'''
Etape 5
Créez une fonction qui permet de tirer de manière aléatoire une personne.

'''
import random

def randomPerson(populations):
    person_random = random.choice(populations)
    return person_random

# Exemple d'utilisation de la fonction
person_choice = randomPerson(populations)

print(f"Personne tirée aléatoirement : {person_choice['name']} avec une valeur de rate de {person_choice['rate']}.")

'''
Etape 6
Ordonnez par ordre croissant dans une liste 's' de tuples, les personnes en fonction de leur rate respectif.

'''
s=[]

# Créer un tableau en ordre décroissant
tab_order = sorted(populations,key=lambda person: person['rate'])

s = [(person['name'], person['rate']) for person in tab_order]

# Affichez la liste triée
for person in tab_order:
    print(f"{person['name']} a une valeur de rate de {person['rate']}.")


'''
Etape 7
Trouvez la valeur centrale, la valeur centrale partage en deux la série de valeurs rates ordonnées.

'''

# Importer median depuis statistics

from statistics import median

# Tableau ordonnée en ordre croissant
tab_order = sorted(populations,key=lambda person: person['rate'], reverse=True)

# Stocker les valeur chaque personne dans un nouveau tableau

tab_rate = [person['rate'] for person in populations]

# Appliquer la méthode median() sur ce nouveau tableau

print(f"La valeur centrale est {median(tab_rate)}")


'''
Etape 8
Trouvez la valeur centrale, la valeur centrale partage en deux la série de valeurs rates ordonnées.

'''

# Supposons que liste_triee_s soit la liste des tuples (nom, rate) triée par ordre croissant en fonction de la valeur de 'rate'

# Trouvez la médiane
nombre_personnes = int(len(tab_rate))

if nombre_personnes % 2 == 1:
    # Si le nombre de personnes est impair
    mediane = tab_rate[int (nombre_personnes) // 2][1]
else:
    # Si le nombre de personnes est pair
    mediane = (tab_rate[int (nombre_personnes) // 2 - 1][1] +
               tab_rate[int (nombre_personnes) // 2][1]) / 2

# Partitionnez la liste en quatre parties distinctes en utilisant la médiane
partie1 = [personne for personne in tab_rate if personne[1] < mediane]
partie2 = [personne for personne in tab_rate if personne[1] == mediane]
partie3 = [personne for personne in tab_rate if personne[1] > mediane]
partie4 = [personne for personne in tab_rate if personne[1] > mediane]

# Affichez les parties
print("Partie 1 :", partie1)
print("Partie 2 :", partie2)
print("Partie 3 :", partie3)
print("Partie 4 :", partie4)


    



